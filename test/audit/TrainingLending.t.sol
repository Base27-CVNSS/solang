// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;
import "../../examples/audit/TrainingLending.sol";

/// @notice Foundry test không cần forge-std, không có giao dịch tài chính thật.
contract TrainingLendingAuditTest {
    function test_ReproducesBugOnToyState() public {
        TrainingLendingBuggy vault = new TrainingLendingBuggy();
        vault.deposit(100);
        vault.borrow(100);
        require(vault.healthy(address(this)), "precondition");
        vault.withdraw(100);
        require(!vault.healthy(address(this)), "expected toy invariant violation");
    }

    function test_PatchPreventsUnsafeWithdrawal() public {
        TrainingLendingPatched vault = new TrainingLendingPatched();
        vault.deposit(100);
        vault.borrow(100);
        (bool ok,) = address(vault).call(
            abi.encodeWithSelector(vault.withdraw.selector, uint256(100))
        );
        require(!ok, "should revert");
        require(vault.healthy(address(this)), "post-invariant");
        require(vault.collateral(address(this)) == 100, "rollback failed");
    }

    function testFuzz_PatchedWithdrawalStaysHealthy(
        uint64 rawAmount, uint64 rawDebt, uint64 rawWithdrawal
    ) public {
        TrainingLendingPatched vault = new TrainingLendingPatched();
        uint256 amount = uint256(rawAmount % 100000) + 1;
        uint256 maxDebt = amount * 150 / 100;
        uint256 borrowAmount = uint256(rawDebt) % (maxDebt + 1);
        vault.deposit(amount);
        if (borrowAmount > 0) vault.borrow(borrowAmount);
        uint256 withdrawal = uint256(rawWithdrawal) % (amount + 1);
        (bool ok,) = address(vault).call(
            abi.encodeWithSelector(vault.withdraw.selector, withdrawal)
        );
        // Bất kể call thành công hay revert, state sau transaction phải hợp lệ.
        require(vault.healthy(address(this)), "bad patched state");
        if (!ok) require(vault.collateral(address(this)) == amount, "failed call changed state");
    }
}

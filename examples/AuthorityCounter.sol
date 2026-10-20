// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
import "solana";
contract AuthorityCounter {
    address authority;
    uint64 counter;
    constructor(address initialAuthority) { authority = initialAuthority; }
    @signer(admin)
    function increment() external {
        assert(tx.accounts.admin.is_signer);
        assert(tx.accounts.admin.key == authority);
        counter += 1;
    }
    function get() public view returns (uint64) { return counter; }
}

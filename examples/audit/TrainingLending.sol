// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @notice LAB ONLY — chỉ cập nhật mapping số nguyên, KHÔNG nhận/chuyển token/ETH.
contract TrainingLendingBuggy {
    mapping(address => uint256) public collateral;
    mapping(address => uint256) public debt;

    function deposit(uint256 amount) public {
        require(amount > 0, "amount");
        collateral[msg.sender] += amount;
    }

    function borrow(uint256 amount) public {
        require(amount > 0, "amount");
        require(debt[msg.sender] + amount <= collateral[msg.sender] * 150 / 100, "health");
        debt[msg.sender] += amount;
    }

    function withdraw(uint256 amount) public virtual {
        require(collateral[msg.sender] >= amount, "collateral");
        collateral[msg.sender] -= amount;
        // CỐ Ý CÓ LỖ HỔNG TRONG BÀI HỌC: không kiểm tra nợ sau khi rút.
    }

    function healthy(address who) public view returns (bool) {
        return debt[who] <= collateral[who] * 150 / 100;
    }
}

/// @notice Bản vá dành riêng cho toy; không phải lending implementation production.
contract TrainingLendingPatched is TrainingLendingBuggy {
    function withdraw(uint256 amount) public override {
        require(collateral[msg.sender] >= amount, "collateral");
        collateral[msg.sender] -= amount;
        require(healthy(msg.sender), "unhealthy withdrawal");
    }
}

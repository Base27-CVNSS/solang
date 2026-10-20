// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
contract Flipper {
    bool private value;
    constructor(bool initialValue) { value = initialValue; }
    function flip() public { value = !value; }
    function get() public view returns (bool) { return value; }
}

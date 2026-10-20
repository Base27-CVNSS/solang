# 01 · Solidity căn bản

Học ngữ pháp, hàm, state, types, quyền và test

> Tài liệu giảng dạy tiếng Việt. Các đoạn mã cần biên dịch/kiểm tra theo phiên bản Solang đã cài. Dùng local validator hoặc Devnet, tuyệt đối không dùng khóa mainnet.

## 01.01 Cấu trúc Solidity

**Cần nắm:** pragma, contract, state, constructor, function. Bắt đầu bằng Flipper có bool, flip(), get(). Trên Solana trạng thái không ở account chứa executable.

**Dành cho Dev Solidity/EVM:** Cú pháp Solidity dùng được một phần, nhưng target Solana không có toàn bộ EVM builtins.

**Bài thực hành:** Viết Flipper.sol; compile và ghi số byte data account compiler báo.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
contract Flipper {
    bool private value;
    constructor(bool initialValue) { value = initialValue; }
    function flip() public { value = !value; }
    function get() public view returns (bool) { return value; }
}
```

**Câu hỏi tự kiểm tra:** view có được thay đổi state?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 01.02 Kiểu dữ liệu và số học

**Cần nắm:** Nắm bool, uint, int, bytes, string, address, struct. Ưu tiên uint64 cho dữ liệu nằm trong phạm vi 64-bit; uint256 có thể tiêu thụ thêm CU.

**Dành cho Dev Solidity/EVM:** Solana address 32 byte, literal có dạng address"Base58...".

**Bài thực hành:** Thiết kế struct cho hồ sơ đo đạc có id, version, mm, timestamp.

**Câu hỏi tự kiểm tra:** uint256 luôn tối ưu trên SVM?

<details><summary>Mở đáp án</summary>

Không, thường 64-bit hiệu quả hơn.

</details>

---

## 01.03 Hàm và visibility

**Cần nắm:** Phân biệt public, external, internal, private, view và pure. Biên giới external đặc biệt quan trọng vì client cung cấp account metas.

**Dành cho Dev Solidity/EVM:** Revert message và exception trên target Solana khác EVM.

**Bài thực hành:** Viết hàm tăng biến đếm với điều kiện biên.

**Câu hỏi tự kiểm tra:** Có thể tin lỗi revert message hiển thị như ethers EVM?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 01.04 State, storage và layout

**Cần nắm:** Biến trạng thái được serialize trong tài khoản dữ liệu. Việc nâng cấp chương trình phải bảo đảm cấu trúc cũ tương thích hoặc migration rõ ràng.

**Dành cho Dev Solidity/EVM:** EVM gộp code/storage ở contract account; Solana tách program và data account.

**Bài thực hành:** Vẽ schema data V1 rồi bổ sung field V2, mô tả migration.

**Câu hỏi tự kiểm tra:** Upgrade code tự nâng cấp mọi record cũ?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 01.05 Event, log và kiểm tra state

**Cần nắm:** Log hỗ trợ quan sát, không thay thế đọc lại trạng thái. Luôn liên kết event với signature và confirmed transaction.

**Dành cho Dev Solidity/EVM:** Không giả định indexer đọc log y hệt EVM ABI.

**Bài thực hành:** Mô tả log cập nhật hồ sơ và quy trình verify.

**Câu hỏi tự kiểm tra:** Chỉ log thành công là bằng chứng duy nhất của ghi state?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 01.06 Viết và kiểm thử Flipper

**Cần nắm:** Tạo getter và toggle, thử sai/thành công trên validator. Thêm điều kiện kiểm soát khi mở rộng.

**Dành cho Dev Solidity/EVM:** Kiểm soát owner EVM bằng msg.sender không port nguyên trạng.

**Bài thực hành:** Viết 3 testcase: initial, flip một lần, flip hai lần.

**Câu hỏi tự kiểm tra:** Có thể gọi msg.sender trên Solang Solana?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

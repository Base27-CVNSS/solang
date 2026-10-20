# 02 · Từ EVM sang SVM

Account-centric, signer, annotation, PDA và CPI

> Tài liệu giảng dạy tiếng Việt. Các đoạn mã cần biên dịch/kiểm tra theo phiên bản Solang đã cài. Dùng local validator hoặc Devnet, tuyệt đối không dùng khóa mainnet.

## 02.01 Program account và data account

**Cần nắm:** Program chứa SBF executable; data account giữ storage và được program sở hữu. Nhiều data account có thể dùng cùng program.

**Dành cho Dev Solidity/EVM:** Khác contract address gộp code và storage ở Ethereum.

**Bài thực hành:** Vẽ program A và hai account dữ liệu A1/A2.

**Câu hỏi tự kiểm tra:** Program và data account là một?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 02.02 Signer, owner và writable

**Cần nắm:** Signer là tài khoản ký; owner là program có quyền với dữ liệu; writable quyết định quyền ghi của một instruction. Cần kiểm tra quan hệ giữa các account.

**Dành cho Dev Solidity/EVM:** Không thể dùng một AccountMeta bất kỳ để thay thế msg.sender.

**Bài thực hành:** Thiết kế negative tests cho signer giả và owner sai.

**Câu hỏi tự kiểm tra:** Một signer bất kỳ có thể thành admin chỉ vì có chữ ký?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 02.03 Authority thay msg.sender

**Cần nắm:** Dùng @signer(admin), sau đó assert admin.key == authority lưu trong state. Chữ ký và danh tính cho phép là hai điều kiện khác nhau.

**Dành cho Dev Solidity/EVM:** Thay require(msg.sender==owner) bằng signer + so khớp pubkey.

**Bài thực hành:** Đọc examples/AuthorityCounter.sol, tìm điều kiện auth.

```solidity
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
```

**Câu hỏi tự kiểm tra:** Chỉ cần @signer là đủ kiểm soát administrator?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 02.04 Account annotations và IDL

**Cần nắm:** @account đọc, @mutableAccount ghi, @signer ký, @mutableSigner ký+ghi, @payer dùng trong constructor. Client phải theo đúng IDL account order.

**Dành cho Dev Solidity/EVM:** Không có transaction parameters kiểu ABI EVM độc lập với account list.

**Bài thực hành:** Ghi thứ tự và flag cho mỗi account trong IDL sau compile.

```solidity
import "solana";
contract AccountLab {
    @account(readMe)
    @signer(authority)
    @mutableAccount(output)
    function inspect() external view returns (address) {
        assert(tx.accounts.authority.is_signer);
        return tx.accounts.readMe.key;
    }
}
```

**Câu hỏi tự kiểm tra:** Có thể đảo account metas tùy ý?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 02.05 PDA, seed và bump

**Cần nắm:** PDA suy ra từ seeds + program ID và không có private key thường. Chọn seed theo namespace, owner/id và version; validate derivation.

**Dành cho Dev Solidity/EVM:** CREATE2 và PDA đều deterministic nhưng hoạt động khác.

**Bài thực hành:** Thiết kế seeds cho record theo owner + recordId.

**Câu hỏi tự kiểm tra:** PDA được ký như keypair ví thông thường?

<details><summary>Mở đáp án</summary>

Không, runtime xử lý thông qua invoke_signed/CPI thích hợp.

</details>

---

## 02.06 Cross-Program Invocation (CPI)

**Cần nắm:** Gọi chương trình khác cần AccountMeta đúng flags và đúng thứ tự. Runtime kiểm tra privilege escalation; luôn đối chiếu program ID được tin cậy.

**Dành cho Dev Solidity/EVM:** External call Solidity EVM không đòi client cung cấp danh sách account tương tự.

**Bài thực hành:** Vẽ CPI sang SPL Token Program gồm mint, account và authority.

**Câu hỏi tự kiểm tra:** CPI có thể nâng read-only thành writable tùy thích?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

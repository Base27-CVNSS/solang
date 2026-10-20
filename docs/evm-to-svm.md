# Bảng chuyển đổi Solidity / EVM sang Solang / SVM

| Chủ đề | EVM Solidity | Solang target Solana | Cách chuyển |
|---|---|---|---|
| Code và state | Một contract account chứa code và storage | Program account chứa SBF, data account chứa state | Thiết kế account schema rõ ràng |
| msg.sender | Có | Không có | Account signer + so khớp authority |
| msg.value | Có | Không hỗ trợ | Giao dịch/CPI chuyển SOL riêng |
| Address | 20 byte | 32 byte | Dùng Solana pubkey / Base58 |
| ABI | ABI 4 byte selector | IDL, discriminator thường 8 byte, Borsh | Đọc IDL thực tế |
| Deployment | EVM bytecode | ELF/SBF .so | Compiler Solang + Solana CLI |
| Gas | Gas limit, gas price | Compute Units, CU price | Simulate và benchmark |
| ERC20 | Contract triển khai riêng | SPL Token Program và mint/token accounts | Không copy ERC20 |
| External calls | EVM CALL | CPI với AccountMeta | Kiểm tra đúng cờ và thứ tự |
| Upgrade | Proxy hoặc kiểu khác | Upgrade authority (program upgradeable) | Quản lý khóa và layout |

## Ví dụ bảo vệ authority

EVM thường viết: `require(msg.sender == owner)`.

Trên Solang/Solana cần kiểm tra **hai điều kiện**: chữ ký và pubkey trùng authority đáng tin cậy:

```solidity
@signer(admin)
function update() external {
    assert(tx.accounts.admin.is_signer);
    assert(tx.accounts.admin.key == authority);
    // cập nhật state
}
```

> Chỉ dùng @signer không đủ. AccountMeta do client đưa vào có thể là account khác, vì thế phải kiểm tra quan hệ với state/định danh tin cậy.

## Mô hình pipeline 6 bước

1. Viết code Solidity và khai báo account annotations phù hợp.
2. Compile: Solang + LLVM → SBF (.so) + IDL JSON.
3. Deploy với Solana CLI lên local validator hoặc Devnet.
4. Client dựng instruction data + AccountMeta + chữ ký và gửi qua RPC.
5. SVM kiểm tra chữ ký, quyền, account ownership; chạy SBF/CPI dưới compute budget.
6. Xác minh commit hoặc rollback, fee, logs, signature và đọc lại state.

Nguồn tham khảo: https://solang.readthedocs.io/en/latest/targets/solana.html

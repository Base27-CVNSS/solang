# Sáu tầng Solang pipeline — giải thích kỹ thuật và cách debug

Khung học dựa trên hai tài liệu pipeline đã cung cấp: viết code → compiler LLVM → deploy → client → SVM → kết quả. Từng tầng có đầu vào, đầu ra và lỗi riêng.

## Giai đoạn 1: Viết Solidity

**Đầu vào:** yêu cầu nghiệp vụ, quy tắc truy cập, schema account. **Đầu ra:** `.sol` có các hàm và annotation phù hợp target Solana. Cần biết account nào tồn tại, được ai sở hữu, writable ra sao và ai ký. Trong Solidity/EVM người học quen `msg.sender`; trên Solana không có biến đó; dùng `@signer(name)` kết hợp key trùng authority.

**Debug:** Nếu logic cần chuyển native value, đừng viết `msg.value`. Nếu dùng địa chỉ EVM hex, kiểm tra lại Solana pubkey 32 byte/Base58.

## Giai đoạn 2: Solang compiler → LLVM → SBF + IDL

**Đầu vào:** `.sol`, version compiler, flag `--target solana`. **Đầu ra:** binary SBF `.so` và metadata JSON IDL. Phân biệt bản metadata JSON với EVM ABI. Đọc `-v` để xem hợp đồng và kích thước state account. `-O none|less|default|aggressive` là mức tối ưu LLVM; không khẳng định `aggressive` luôn giảm CU.

```bash
solang compile --target solana -v -O default -o build examples/Flipper.sol
```

**Debug:** Sai target, thiếu import, lỗi pragma/cú pháp, giới hạn target. Đầu tiên xác nhận `solang --version` và mã tối giản.

## Giai đoạn 3: Deploy Program

**Đầu vào:** SBF binary, cấu hình Solana CLI, keypair test, SOL thử (rent + fee). **Đầu ra:** Program ID, program data/upgrade authority nếu là chương trình upgradeable. Program không tự động là tất cả data accounts: cần thiết kế và tạo tài khoản dữ liệu khi gọi constructor hoặc qua client.

```bash
solana config get
solana program deploy build/Flipper.so
```

**Debug:** Sai cluster, thiếu SOL, sai program keypair, lỗi upgrade authority.

## Giai đoạn 4: Client tạo Instruction

**Đầu vào:** IDL thực tế, pubkeys, transaction signers, input args. **Đầu ra:** serialized instruction, AccountMeta và giao dịch đã ký. Theo kiểu Anchor-compatible, discriminator thường 8 byte và các tham số có thể được encode Borsh. Thứ tự IDL và flags phải trùng; không tự tạo EVM ABI encoder.

**Debug:** `MissingSignature` → kiểm tra signer; `InvalidAccountData` → owner/type/layout; missing/wrong account → IDL ordering. Trước khi broadcast nên simulate.

## Giai đoạn 5: SVM Runtime

**Đầu vào:** transaction đã ký và trạng thái account tại slot xử lý. Runtime kiểm tra signature, ownership/privileges, rent/lifecycle và giới hạn Compute Units, sau đó dispatch chương trình, thực hiện CPI và áp dụng invariant. Một transaction có nhiều instructions nên ngân sách CU phụ thuộc cấu hình và rules runtime; giá trị 200.000 CU/instruction và tổng 1.400.000 CU là *mốc tham khảo*, phải kiểm tra phiên bản network/SDK chứ không hardcode logic an toàn vào đó.

**Debug:** vượt CU, nâng quyền bất hợp lệ, sai account ownership, CPI tới chương trình ngoài danh sách tin cậy.

## Giai đoạn 6: Thành công hoặc rollback

**Đầu vào:** execution result. **Đầu ra:** signature, err/logs, trạng thái sau xử lý nếu thành công. Giao dịch lỗi có thể mất transaction fee. Một chữ ký giao dịch không đủ để khẳng định state đã thay đổi: kiểm tra confirmation và state read-back.

**Debug:** so sánh dữ liệu trước/sau, đơn vị CU, logs, err code và chương trình thực thi. Lưu signature trong báo cáo lab.

## Bảng quyết định khắc phục

| Hiện tượng | Đầu tiên kiểm tra | Không nên làm |
|---|---|---|
| Compiler báo lỗi | target, version, import, syntax | Sửa ngẫu nhiên IDL |
| Thiếu chữ ký | AccountMeta và keypair | Tăng Compute Unit Limit |
| InvalidAccountData | Owner/type/schema, account order | Bỏ ownership check |
| Vượt CU | Loop, serialization, compute budget | Tăng CU vô hạn |
| Sai số dư | Lamports, fee/rent, transaction confirmation | Giả định giá trị từ msg.value |
| Dữ liệu không đổi | đúng account, writable, rollback? | Chỉ đọc console logs |

**Tham khảo:** https://solang.readthedocs.io/en/latest/running.html · https://solang.readthedocs.io/en/latest/targets/solana.html · https://solana.com/docs

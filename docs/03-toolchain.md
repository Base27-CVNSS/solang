# 03 · Pipeline Solang

Compiler SBF, IDL, local validator, deploy và logs

> Tài liệu giảng dạy tiếng Việt. Các đoạn mã cần biên dịch/kiểm tra theo phiên bản Solang đã cài. Dùng local validator hoặc Devnet, tuyệt đối không dùng khóa mainnet.

## 03.01 Cài đặt Solang CLI

**Cần nắm:** Lấy binary chính thức hoặc Docker, ghi phiên bản đã dùng. Kiểm tra solang --version, solang compile --help và extension editor.

**Dành cho Dev Solidity/EVM:** Không nhầm solc/Foundry EVM với Solang compiler.

**Bài thực hành:** Cài trên máy hoặc container và chụp output --version.

```bash
solang --version
solang compile --help
solana --version
```

**Câu hỏi tự kiểm tra:** Cài solc là đã có compiler SBF?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 03.02 Solang, LLVM, SBF và IDL

**Cần nắm:** Lệnh solang compile --target solana -v -o build examples/Flipper.sol. Compiler sinh executable SBF .so và metadata Anchor-compatible IDL JSON. Đọc file được sinh thực tế.

**Dành cho Dev Solidity/EVM:** EVM bytecode + ABI không bằng SBF + IDL.

**Bài thực hành:** So sánh tên instruction, tài khoản, metadata trong IDL.

```bash
mkdir -p build
solang compile --target solana -v -o build examples/Flipper.sol
# Đọc .so và .json do compiler sinh ra; không đoán IDL.
```

**Câu hỏi tự kiểm tra:** IDL chứa private key?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 03.03 Local validator và Devnet

**Cần nắm:** solana-test-validator dùng test địa phương; solana config set --url localhost hoặc devnet quyết định cluster. Không dùng tiền thật và địa chỉ ví mainnet.

**Dành cho Dev Solidity/EVM:** RPC nhầm cluster là lỗi vận hành phổ biến.

**Bài thực hành:** Ghi solana config get, balance và logs của validator.

```bash
solana-test-validator
# Mở terminal khác:
solana config set --url localhost
solana config get
```

**Câu hỏi tự kiểm tra:** Giao dịch Devnet tiêu dùng SOL thật?

<details><summary>Mở đáp án</summary>

Không, Devnet là mạng thử nghiệm.

</details>

---

## 03.04 Deploy và quyền nâng cấp

**Cần nắm:** solana program deploy build/<contract>.so đăng ký program; quản lý program ID và upgrade authority. Không thu hồi quyền nâng cấp trước khi hiểu hậu quả.

**Dành cho Dev Solidity/EVM:** Khác các mô hình proxy upgrade EVM.

**Bài thực hành:** Deploy local, lấy program ID và đọc thông tin authority.

```bash
# Chạy sau khi biên dịch và xác nhận đúng cluster:
solana program deploy build/Flipper.so
solana program show PROGRAM_ID
```

**Câu hỏi tự kiểm tra:** Bỏ upgrade authority rồi có thể luôn sửa binary?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 03.05 Sáu tầng pipeline thực thi

**Cần nắm:** Solidity → Solang LLVM/SBF + IDL → Deploy → client build instruction → SVM validate/run → commit hoặc rollback. Các tầng có logs và lỗi khác nhau.

**Dành cho Dev Solidity/EVM:** Gas EVM khác Compute Units; ABI EVM khác Borsh/IDL.

**Bài thực hành:** Trace một transaction từ source đến trạng thái cuối cùng.

**Câu hỏi tự kiểm tra:** Gửi RPC trả về signature đã đủ xác nhận?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 03.06 Debug: build, deploy, runtime

**Cần nắm:** Kiểm tra diagnostic compiler; RPC và fee khi deploy; signer, writable, owner, account order, program ID và CU khi runtime. Tạo minimal reproduction.

**Dành cho Dev Solidity/EVM:** Solidity revert strings không nhất thiết xuất hiện giống EVM.

**Bài thực hành:** Chẩn đoán MissingSignature và InvalidAccountData theo checklist.

**Câu hỏi tự kiểm tra:** Tăng CU sẽ sửa MissingSignature?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

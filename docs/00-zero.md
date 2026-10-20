# 00 · Nền tảng từ số 0

Nắm Web3, ví, JS/TS, Git và tư duy bảo mật

> Tài liệu giảng dạy tiếng Việt. Các đoạn mã cần biên dịch/kiểm tra theo phiên bản Solang đã cài. Dùng local validator hoặc Devnet, tuyệt đối không dùng khóa mainnet.

## 00.01 Web2, Web3 và dApp

**Cần nắm:** Blockchain là một máy trạng thái phi tập trung. DApp gồm frontend, ví, RPC, logic on-chain và dữ liệu off-chain. Đừng đồng nhất blockchain với website.

**Dành cho Dev Solidity/EVM:** EVM và Solana đều có on-chain program nhưng kiến trúc dữ liệu khác.

**Bài thực hành:** Vẽ luồng người dùng ký giao dịch rồi đọc kết quả trên explorer.

**Câu hỏi tự kiểm tra:** DApp có bắt buộc chứa tất cả dữ liệu trên chain?

<details><summary>Mở đáp án</summary>

Không, dữ liệu lớn và riêng tư thường đặt ngoài chain.

</details>

---

## 00.02 Block, giao dịch, xác nhận

**Cần nắm:** Gửi transaction tới RPC không chứng minh nó đã thực thi thành công. Cần kiểm tra confirmation, err, logs và trạng thái sau khi chạy.

**Dành cho Dev Solidity/EVM:** Không áp máy móc số block confirmations Ethereum cho Solana.

**Bài thực hành:** Tra một transaction Devnet, ghi signature, slot và lỗi nếu có.

**Câu hỏi tự kiểm tra:** RPC trả signature nghĩa là giao dịch thành công?

<details><summary>Mở đáp án</summary>

Không, còn phải xác minh tình trạng xử lý.

</details>

---

## 00.03 Ví, public key và chữ ký số

**Cần nắm:** Private key tạo chữ ký, public key định danh tài khoản. Transaction có thể yêu cầu nhiều signer. Không đưa khóa ví vào Git hay trình duyệt lạ.

**Dành cho Dev Solidity/EVM:** Địa chỉ Ethereum thông thường 20 byte, Solana public key 32 byte.

**Bài thực hành:** Tạo ví test, ghi pubkey và lập quy trình giữ seed/private key an toàn.

**Câu hỏi tự kiểm tra:** isSigner=true tự tạo ra chữ ký?

<details><summary>Mở đáp án</summary>

Không, phải có chữ ký hợp lệ hoặc PDA signing phù hợp.

</details>

---

## 00.04 JavaScript và TypeScript nền tảng

**Cần nắm:** Học biến, function, async/await, Promise, Uint8Array, đối tượng JSON và bigint/BN. RPC dùng dữ liệu nhị phân và số lớn nên tránh Number thiếu chính xác.

**Dành cho Dev Solidity/EVM:** Solidity là logic on-chain; TypeScript vận hành client.

**Bài thực hành:** Viết async function giả lập gọi RPC và xử lý timeout.

**Câu hỏi tự kiểm tra:** Có nên tùy tiện dùng Number cho mọi giá trị u64?

<details><summary>Mở đáp án</summary>

Không, lựa chọn bigint/BN theo SDK.

</details>

---

## 00.05 Terminal, Git và môi trường

**Cần nắm:** Biết cd, ls, git status, git add, git commit, .gitignore; ghi lại phiên bản SDK/compiler để tái hiện lỗi.

**Dành cho Dev Solidity/EVM:** solc trên EVM không tương đương compile --target solana.

**Bài thực hành:** Tạo repository thử nghiệm và loại bỏ secret khỏi commit.

**Câu hỏi tự kiểm tra:** Không ghi version thì lỗi build có dễ tái lập?

<details><summary>Mở đáp án</summary>

Không, môi trường cần được cố định.

</details>

---

## 00.06 Bảo mật đầu tiên

**Cần nắm:** Liệt kê tài sản, ranh giới tin cậy, kẻ tấn công: ví bị chiếm, malicious program, account giả, quyền nâng cấp bị lộ.

**Dành cho Dev Solidity/EVM:** Bảo mật Solana cần nhìn signer, owner, writable và CPI bên cạnh logic ứng dụng.

**Bài thực hành:** Viết threat model 5 dòng cho một dApp ghi vị trí.

**Câu hỏi tự kiểm tra:** Simulation đủ để bảo đảm dApp an toàn?

<details><summary>Mở đáp án</summary>

Không, cần test và audit.

</details>

---

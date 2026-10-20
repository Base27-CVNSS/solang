# Solang Academy Việt Nam 🇻🇳

**Khóa học Solidity → Solang → Solana bằng tiếng Việt, từ số 0 đến nâng cao.**

🌐 [Mở học viện trực tuyến](https://base27-cvnss.github.io/solang/) · [Tài liệu Solang](https://solang.readthedocs.io/en/latest/) · [Solana Docs](https://solana.com/docs)

## Mục tiêu

- Lộ trình **Zero → Developer**: lập trình, blockchain, Solidity, Solana và công cụ.
- Lộ trình **EVM → SVM**: hiểu chính xác mô hình account, signer, PDA, CPI, CU, IDL; không giả định Solidity trên Ethereum chạy nguyên trạng.
- Tổ chức theo **pipeline sáu bước**: viết Solidity → biên dịch Solang/LLVM → deploy → client → SVM → kết quả.
- **Học bằng trình duyệt**: giao diện tiếng Việt, tìm kiếm, đánh dấu đã học, kiểm tra kiến thức, ví dụ có nút sao chép; giao diện dùng được offline sau khi tải HTML.

## Trước khi bắt đầu

Solang là **trình biên dịch Solidity cho nhiều target**, còn Solana chạy **SBF** với mô hình **account riêng**. Một chương trình Solana thường tách mã thực thi và các tài khoản chứa trạng thái. Solang không phải EVM emulator. Không có `msg.sender` hay `msg.value` với target Solana; `payable` không tạo cơ chế chuyển SOL như EVM.

Dùng **local validator/Devnet**, ví thử và dữ liệu giả khi thực hành; **không dùng khóa riêng thật**. Mọi ví dụ chưa được tự động biên dịch/kiểm thử trong repository này là *mã minh họa*, cần đối chiếu với phiên bản công cụ được cài và đặc tả IDL được tạo ra trước khi triển khai.

## Cấu trúc nội dung

| Cấp | Học phần | Trọng tâm |
|---|---|---|
| Zero | 00 — Khởi động | Blockchain, ví, JavaScript, CLI, Git, kiến thức bảo mật |
| Cơ bản | 01 — Solidity nền tảng | Kiểu dữ liệu, hàm, storage, access control, tests |
| Chuyển đổi | 02 — EVM sang SVM | Program/account, authority, annotation, PDA, CPI, rent |
| Công cụ | 03 — Solang pipeline | Compiler, LLVM/SBF, IDL, validator, deploy, log |
| Ứng dụng | 04 — Fullstack | Client TypeScript, AccountMeta, Borsh, SPL, UI |
| Nâng cao | 05 — Security & Architecture | Kiểm tra tài khoản, mô hình đe dọa, fuzz, tối ưu CU, nâng cấp, dự án cuối khóa |

Xem danh sách **36 bài học tương tác** tại `index.html` và tài liệu chi tiết trong `docs/`; mã minh họa trong `examples/`.

## Chạy website

Chỉ cần mở `index.html` trong trình duyệt (không cần máy chủ hoặc CDN); để dùng GitHub Pages: **Settings → Pages → Deploy from a branch → main / (root)**.

## Compile ví dụ Solang (khi đã cài)

```bash
solang --version
solang compile --target solana -v -o build examples/Flipper.sol
```

Đầu ra phụ thuộc phiên bản compiler. Sau khi biên dịch hãy mở **IDL JSON được sinh thực tế** để xem instruction và account order, không hardcode ABI EVM hay giả định discriminator giống nhau cho mọi phiên bản.

## Tài liệu đối chiếu

- https://solang.readthedocs.io/en/latest/targets/solana.html
- https://solang.readthedocs.io/en/latest/installing.html
- https://solang.readthedocs.io/en/latest/running.html
- https://github.com/hyperledger-solang/solang
- https://solana.com/docs/programs
- https://github.com/solana-foundation/program-examples

> **Ghi chú:** Quy trình, cú pháp, API, phiên bản Solang/Anchor/Solana SDK có thể thay đổi. Các tài liệu mang tính đào tạo; không phải bảo đảm bảo mật hoặc hướng dẫn triển khai mainnet mà không audit.

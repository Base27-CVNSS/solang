# Solang Academy Việt Nam 🇻🇳

**54 bài, 7 học phần tiếng Việt: Solidity → Solang → Solana → Smart Contract Economic Security & Elite Audit.**

🌐 [Mở tệp website học tập](https://github.com/Base27-CVNSS/solang/blob/main/index.html) · [Tài liệu Solang](https://solang.readthedocs.io/en/latest/) · [Solana Docs](https://solana.com/docs)

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
| Elite Audit | 06 — Top 500 (mục tiêu phấn đấu) | 18 bài: EVM internals, two adversarial mindsets, economic modeling, fuzz, formal, PoC và report |

Xem danh sách **54 bài học tương tác** tại `index.html` và tài liệu chi tiết trong `docs/`; mã minh họa trong `examples/`.

**Tài liệu chuyên sâu:** [8 bước chuyển EVM→SVM](docs/chuyen-doi-solidity-svm-chuyen-sau.md) · [Pipeline sáu giai đoạn](docs/pipeline-sau-giai-doan.md) · [Red-Team checklist](docs/redteam-checklist.md) · [GeoPIN capstone](docs/capstone-geopin.md) · [Cài đặt](docs/setup.md).

## Chạy website

Chỉ cần tải và mở `index.html` trong trình duyệt (không cần máy chủ hoặc CDN). **GitHub Pages chưa được xác nhận kích hoạt**; để xuất bản dưới tên miền `base27-cvnss.github.io/solang/`, vào **Settings → Pages → Deploy from a branch → main / (root)** rồi kiểm tra URL hoạt động.

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


## 06 — Elite Auditor / mục tiêu Top 500 kỹ sư bảo mật

Đã bổ sung **18 bài chuyên sâu**, đưa tổng giáo trình lên **54 bài / 7 học phần**. Xem [Học phần 06](docs/06-top500-auditor.md), [Playbook audit](docs/06-audit-workflow-playbook.md), [Bất biến kinh tế](docs/06-economic-invariants.md), [EVM vs SVM audit](docs/06-svm-audit-boundaries.md), [Mẫu finding](docs/06-finding-template.md), [Rubric 12 tháng](docs/06-skill-matrix.md) và [Lab Foundry](examples/audit/README.md).

**Lưu ý:** “Top 500” là mục tiêu tự đào tạo, không phải xếp hạng thực chứng. Công cụ EVM không xác nhận trực tiếp binary Solang/SBF; phải test Solana riêng. 10/15/50/20/5 là thời lượng minh họa, không phải định mức chính thức từ Dedaub.

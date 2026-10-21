# Cẩm nang Dev Blockchain 500 mục · 50 nhóm × 10

**Mục đích:** chuyển 500 hạng mục kỹ năng trong đề cương người dùng thành một **bản đồ học tập tự đánh giá** có thể tìm kiếm và làm việc offline. Các mục số 001–500 đi theo **đúng thứ tự 50 nhóm trong bản thảo**. Tên chủ đề được biên tập cô đọng, không chép nguyên văn 500 đoạn giải thích; mục tiêu và bài thực hành được thêm với vai trò gợi ý giáo dục.

## Truy cập

- [Giao diện offline 500 năng lực](../dev-handbook.html)
- [JSON 500 mục dùng cho dashboard](../dev-handbook.json)
- [Học viện 64 bài Solang](../index.html)
- [18 bài Security Audit chuyên sâu](06-top500-auditor.md)
- [100 gương điển hình Auditor](../auditors.html)
- [Phương trình Blockchain](07-blockchain-equation.md)

## 5 lộ trình

| Lộ trình | Trọng tâm | Bằng chứng cuối |
|---|---|---|
| Smart Contract Developer | Solidity, token, Foundry, AA, rollup, non-EVM, Solidity→Solang | repo, contracts chạy local, integration tests, verify |
| Security Auditor | Threat model, Solidity/EVM/SVM, fuzz, formal, financial logic, incident response | audit report, regression tests, safe PoC |
| Protocol Researcher | Consensus, game theory, crypto, ZK, rollup, tokenomics, economic ABM | specification, reproducible simulation, research note |
| Infrastructure Engineer | Node/RPC, indexing, IaC, queues, observability, hardening, DR | benchmark + SLO/runbook + chaos test |
| AI × Web3 Engineer | Wallet agents, MCP/A2A, RAG, tool safety, AI audit, DePIN, verified inference | sandbox agent, spend limits, policy tests, audit trail |

Bộ lọc theo lộ trình dùng **nhóm kỹ năng** làm đơn vị. Đây là một gợi ý học tập: cùng một nhóm có thể liên quan đến nhiều vai trò; không dùng để phân loại tuyệt đối.

## Đánh giá theo bằng chứng

| Trạng thái | Ý nghĩa | Tiêu chí chuyển trạng thái |
|---|---|---|
| Chưa học | Chưa tự giải thích được hoặc chưa tiếp cận | Đọc tài liệu, xác định dependency |
| Đang học | Giải thích được mục đích, đang làm lab | Viết note và có test/PoC thử |
| Nắm vững | Có hiện vật kỹ thuật tái lập, giải thích trade-off, threat model | Repo, log, test, benchmark hoặc báo cáo được review |

**Lưu ý:** đánh dấu “nắm vững” trên UI chỉ là **tự đánh giá**, không có kiểm tra hoặc chứng nhận tự động. Bộ đếm trên trang riêng không được cộng vào 64 bài học của học viện.

## Chiến lược học 4 giai đoạn

1. **Kiến thức nền 001–100:** xác định đường đi từ Solidity sang Solana; học kiểm thử, account model, mật mã và threat modeling.
2. **Ứng dụng 101–200:** chọn một chuyên ngành sâu (DePIN, RWA, Bitcoin L2, Restaking, Modular, MEV, AI).
3. **Kỹ thuật hệ thống 201–300:** vận hành, cross-VM, quality assurance, compliance và research.
4. **Biên giới 301–500:** consensus protocol, cryptography, mechanism design, audit, L3, intent-centric, privacy, post-quantum và AI × blockchain.

**Không cần hoàn thành cả 500:** người học chọn 5–12 nhóm phù hợp vai trò, ưu tiên 1 chuyên môn hẹp làm portfolio với code chạy được và public research. Ngành thay đổi nhanh nên mọi “xu hướng 2026” cần đối chiếu ngày, trạng thái EIP/RIP, phiên bản thư viện và tài liệu chính thức.

## Bài tập portfolio dùng lại

- Mỗi 10 mục: chọn 1 vấn đề làm mini-project, nộp 1 README, 1 test âm tính, 1 sơ đồ dữ liệu/quyền hoặc 1 bảng trade-off.
- Mỗi 50 mục: ghi một nghiên cứu tình huống có giả thiết, phép đo, kết quả và giới hạn.
- Cuối một lộ trình: kiểm tra kiến thức với peer review, nêu chính xác điều đã thử và điều chưa được chứng minh.
- Khi công nghệ liên quan tiền thật, ví, validator, MEV hoặc white-hat rescue: **chỉ thực hành trên sandbox do mình kiểm soát hay môi trường được cấp phép**.

## Phân biệt công cụ và target

Foundry/Slither/Echidna/Medusa/Halmos/Certain formal tooling tập trung vào **EVM**; không suy ra program Solang/SBF đã an toàn chỉ vì bản Solidity EVM test PASS. Đối với Solana, phải kiểm tra quyền account, signer, PDA/CPI, IDL và runtime với local validator riêng.

## Chỉnh sửa/đóng góp

Dữ liệu trong `dev-handbook.json` có định danh DEV-001…DEV-500 và `groupId` G01…G50. Muốn thêm link chính thức, thay `source` hoặc thêm `references`, cần đối chiếu sơ cấp, ghi nguồn/ngày xác minh. Không đánh đồng câu mô tả từ người dùng với chứng cứ thực nghiệm độc lập.

## Quyền riêng tư

Tiến độ lưu bằng localStorage trong trình duyệt và chỉ gửi ra ngoài nếu chính người dùng xuất file. Không đăng nhập, không ví, không tài khoản, không thu thập địa chỉ; trang chạy trực tiếp dưới file:// khi tải đủ HTML.
# Playbook 06: Hai tư duy đối kháng × năm giai đoạn audit

> Học liệu nghiên cứu bảo mật theo phương pháp được công bố bởi [Dedaub](https://dedaub.com/blog/web3-audit-methodology/) và [Dedaub docs](https://docs.dedaub.com/docs/audits/smartContractAudits/). Không suy diễn rằng các định mức 10/15/50/20/5 bên dưới do Dedaub ấn định.

## I. Hai tư duy không thể thiếu

**Tư duy A — Defender / Model of Intended Behavior.** Đọc tài liệu, whitepaper, source, dependency, test và phỏng vấn người thiết kế để dựng mô hình: actors, quyền, nguồn số liệu, tài sản, flow tiền, state transition, điều kiện sản phẩm hứa hẹn. Viết **spec có thể kiểm thử**. Ví dụ, tại cuối thao tác `borrow` thành công, khoản nợ mới không vượt ngưỡng LTV tại giá oracle hợp lệ.

**Tư duy B — Adversarial / Subvert Assumptions.** Từng giả định từ A biến thành giả thuyết bác bỏ: “nếu giá stale 1 giờ?”, “nếu rút collateral sau borrow?”, “nếu token thu phí chuyển khoản?”, “nếu admin nâng cấp logic?”, “nếu dùng cùng oracle làm nguồn giá cho hai market liên thông?”. Mục tiêu là **tìm counterexample**, không dựng kịch bản phỏng đoán không chứng minh.

**Challenge partner:** auditor thứ hai tái giải thích mô hình không nhìn ghi chú của người đầu tiên, chất vấn các góc tối; đổi vai và đánh giá đủ góc cạnh cả ở cấp hàm, cấp luồng, cấp protocol và cross-chain. Dedaub mô tả rõ two-phase review, peer challenging và multilevel reasoning.

## II. Quy trình gợi ý (thời gian là ví dụ quản trị)

| Giai đoạn | Đề xuất | Câu hỏi cốt lõi | Artifact |
|---|---:|---|---|
| 1. Scope & threat modeling | 10% | Hệ thống chính thức bảo đảm gì? Ai được phép làm gì? | scope.md; SHA; trust graph |
| 2. Static tools & reconnaissance | 15% | Có tín hiệu nào cần ưu tiên? Phụ thuộc nào chưa kiểm tra? | scanner.json; triage.csv |
| 3. Manual adversarial review | 50% | Giả định nào không được enforce? Tương tác nào bẻ invariant? | hypothesis register; state graph |
| 4. PoC, fuzz và formal checks | 20% | Có phản ví dụ có thể tái chạy không? | deterministic test; logs; counterexample |
| 5. Evidence report | 5% | Root cause, risk, impact, patch đã được xác minh? | finding; severity; fix review |

Phân bổ này dùng làm **thước đo học tập**. Một dự án production có thể cần thời gian khác, nhiều vòng fix review và continuous monitoring.

## III. Checklist người audit giỏi phải tự trả lời

1. Scope gồm **commit SHA nào**, compiler version nào, chain, proxy/implementation nào?
2. Tài sản, nợ phải trả, collateral, LP shares, reserves, fee và “số dư thực” có được hạch toán nhất quán?
3. Ai có thể thay oracle, price feed, risk parameter, implementation, withdrawal pause, multisig?
4. Bất biến được phát biểu **ở thời điểm nào**: mọi trạng thái, cuối một instruction, cuối transaction hay tại phép kiểm borrow/withdraw?
5. Một vị thế có thể thành bad debt do thị trường giảm giá mà không có lỗi code không?
6. Fee-on-transfer/rebasing/decimals/rounding có làm sai giả định ERC20 thuần?
7. External call có làm thay đổi state, callback hoặc reentrancy theo đúng VM không?
8. Thứ tự giao dịch, snapshot, thời điểm block/slot và settlement là giả định bảo mật hay chỉ UI?
9. Tích hợp AMM + lending + oracle có tạo vòng feedback giá hoặc khả năng thao túng không?
10. Khi báo lỗ hổng, đã phân biệt **điều kiện khả thi** và **thiệt hại dự đoán** chưa?
11. PoC chạy trên sandbox/được cấp phép, không gây ảnh hưởng người dùng thật?
12. Patch có regression tests và lộ trình fix review, hay chỉ đổi code mà không tái thử?

## IV. Hypothesis Register

| ID | Intended invariant | Giả định ngầm | Điều kiện đối kháng | Test/PoC | Kết quả | Độ tin cậy |
|---|---|---|---|---|---|---|
| A-01 | sau withdraw hợp lệ debt ≤ LTV × collateral | withdraw luôn tái check health | borrow rồi rút gần hết | Foundry toy | Chờ chạy | Chưa xác nhận |
| A-02 | token reserve phản ánh số token nhận | transfer luôn 1:1 | token thu phí | mock token | Chờ chạy | Chưa xác nhận |
| A-03 | oracle hợp lệ | giá mới, đúng decimals | stale feed | oracle mock | Chờ chạy | Chưa xác nhận |

## V. Bằng chứng tối thiểu cho mỗi finding

```text
source commit → expected behavior → invariant → preconditions
→ input sequence → actual observed state + test output
→ impact bounded by economics and controls
→ patch → replay/regression → residual risk / disclosures
```

Cấm tự biến warning scanner thành finding đã chứng minh. Test chỉ rõ **khả năng sai lệch trong toy không có tiền**, không phải chứng minh exploit trên protocol nào đó.

Nguồn: https://dedaub.com/blog/web3-audit-methodology/ ; https://docs.dedaub.com/docs/audits/smartContractAudits/

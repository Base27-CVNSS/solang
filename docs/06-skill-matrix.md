# Auditor Skill Matrix — 12 tháng hướng đến cấp độ Elite

**“Top 500 kỹ sư toàn cầu” là đích năng lực tự đặt ra.** Không có bảng xếp hạng toàn cầu thống nhất để gán một thứ hạng khách quan cho mọi Smart Contract Auditor. Hệ đánh giá này là đề xuất của Solang Academy, không được Dedaub chứng nhận.

## 4 giai đoạn, mỗi giai đoạn 3 tháng

| Tháng | Trọng tâm | Bằng chứng học tập tối thiểu |
|---|---|---|
| 1–3 | EVM internals, Foundry, bytecode, storage, auth | 3 code maps, 15 regression tests, 2 review toy |
| 4–6 | Slither triage, Echidna/Medusa, Halmos/Certora fundamentals | 3 fuzz campaigns, 10 invariants, 1 formal specification |
| 7–9 | AMM, lending, oracle, MEV, tokenomics và insolvency | 3 economic models, 2 controlled counterexamples, 3 findings |
| 10–12 | Composability, peer review, fix review, Solang/SVM differences | 2 audit reports peer-reviewed, 1 SBF test matrix, 1 capstone |

## Rubric tự đánh giá 100 điểm

| Năng lực | Điểm | Bằng chứng tối đa |
|---|---:|---|
| EVM internals và cross-VM runtime | 15 | Trace storage, calls, owner, SBF boundaries |
| Two adversarial mindsets + peer challenge | 20 | Các giả định phản ví dụ được kiểm thử |
| Economic invariants + stress testing | 20 | Sổ cái, oracle, AMM, lending, incentives |
| Static/fuzz/formal tools | 15 | Logs, replay, false-positive reasoning, assumptions |
| Finding report + fix review | 15 | Root cause, impact, patch, regression |
| Ethics, independent review, communication | 15 | Reviewer ký nhận và responsible disclosure |

**Mốc nội bộ:** 0–49 foundation, 50–69 junior, 70–84 independent, 85–94 senior research track, 95–100 elite research readiness. Mốc này không dự báo vị trí trong ngành.

### Gate bắt buộc dù tổng điểm cao

- Hai báo cáo audit có scope, commit SHA, test và reviewer độc lập.
- Một bất biến kinh tế tìm được counterexample *và* retest bản vá.
- Một bài proof/formal test ghi chính xác assumptions và bounds.
- Một phân tích rủi ro tương tác nhiều giao thức.
- Một ma trận kiểm thử Solang/SVM không lấy kết quả EVM làm bằng chứng thay thế.
- Mọi PoC đều trong phạm vi cho phép, không lấy tài sản hay khóa người khác.

**Cách luyện:** mỗi tuần chọn một protocol toy; tuần 1 mô hình hóa legitimate use, tuần 2 phản biện giả định, tuần 3 test/fuzz, tuần 4 viết finding và làm peer review. Lặp lại ở nhiều thể loại protocol, đo tiến bộ bằng artifact tái lập được.

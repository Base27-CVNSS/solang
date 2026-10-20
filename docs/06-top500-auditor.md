# Học phần 06 — Elite Auditor / Top 500 (mục tiêu năng lực)

**18 bài thực chiến.** “Top 500” không phải thứ hạng được xác nhận bởi tổ chức xếp hạng quốc tế; đo tiến bộ bằng việc hiểu giao thức, xác định economic invariants, viết test có thể tái chạy và báo cáo được peer review.

Dùng hai tư duy A (hiểu ý định) → B (phá giả định), phản biện chéo giữa hai reviewer, kiểm thử kết hợp nhiều thành phần. Xem [Dedaub methodology](https://dedaub.com/blog/web3-audit-methodology/) và [Audit guide](https://docs.dedaub.com/docs/audits/smartContractAudits/).

## 06.01 · Mental Model A: hệ thống phải đúng như thế nào?

**Phân tích chuyên sâu:** Đọc đặc tả, code, quyền, tài sản, state và xây mô hình hành vi hợp pháp. Viết invariant bằng lời và test trước khi tìm bug.

**So sánh/chuyển đổi:** Auditor phải tìm sai lệch với spec, không chỉ so pattern Solidity.

**Bài thực hành có bằng chứng:** Vẽ state machine deposit→borrow→repay→withdraw và viết 5 giả định bắt buộc.

**Câu hỏi:** Vì sao không bắt đầu chỉ bằng chạy scanner?

<details><summary>Giải thích</summary>

Tool không hiểu ý định kinh tế và giả định ngầm.

</details>

---

## 06.02 · Mental Model B: tấn công giả định ngầm

**Phân tích chuyên sâu:** Chuyển sang vai đối kháng: giả sử oracle sai, actor hành động lệch thứ tự, nguồn giá bị trễ, số dư thay đổi bất ngờ.

**So sánh/chuyển đổi:** Type-safe code vẫn có thể thất bại về logic và kinh tế.

**Bài thực hành có bằng chứng:** Lập 12 giả định ngầm và phản ví dụ cụ thể tương ứng.

**Câu hỏi:** Kiểu dữ liệu hợp lệ đồng nghĩa nghiệp vụ an toàn?

<details><summary>Giải thích</summary>

Không, cần kiểm chứng điều kiện giá trị và trạng thái.

</details>

---

## 06.03 · Peer challenge và tương tác nhiều tầng

**Phân tích chuyên sâu:** Hai reviewer giải thích mô hình cho nhau, hoán đổi vai defender/attacker; phân tích lỗi giữa nhiều module và tích hợp ngoài.

**So sánh/chuyển đổi:** Bug hệ thống có thể do sự kết hợp hàm không có lỗi cục bộ.

**Bài thực hành có bằng chứng:** Làm challenge review oracle+AMM+lending và nộp 10 câu chất vấn.

**Câu hỏi:** Một hàm đúng cục bộ bảo đảm protocol đúng toàn cục?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.04 · Scope, trust model và threat graph

**Phân tích chuyên sâu:** Chốt commit SHA, files, actors, privileges, multisig, governance, oracle, bridges và ranh giới tin cậy; ghi out-of-scope.

**So sánh/chuyển đổi:** Không công bố audited toàn bộ khi chỉ review một phần source hoặc binary.

**Bài thực hành có bằng chứng:** Tạo scope.md, trust graph và attack-surface matrix.

**Câu hỏi:** Audit một lần có giá trị mãi mãi?

<details><summary>Giải thích</summary>

Không, code và phụ thuộc có thể thay đổi.

</details>

---

## 06.05 · EVM internals cấp độ máy ảo

**Phân tích chuyên sâu:** Hiểu storage slot, mapping keccak, calldata/memory/storage, CALL, delegatecall, proxy, revert, bytecode và gas.

**So sánh/chuyển đổi:** EVM bytecode khác Solang output SBF; cùng source không đồng nghĩa runtime giống.

**Bài thực hành có bằng chứng:** Vẽ storage layout của proxy và tìm 3 giả định upgrade.

**Câu hỏi:** delegatecall dùng storage của ai?

<details><summary>Giải thích</summary>

Context lưu trữ của caller.

</details>

---

## 06.06 · Slither + static analysis triage

**Phân tích chuyên sâu:** Dùng Slither trên môi trường Solidity/EVM thích hợp; phân biệt tín hiệu, false positive, exploitable state và giới hạn detector.

**So sánh/chuyển đổi:** Tool EVM không phải chứng nhận binary Solang/SBF.

**Bài thực hành có bằng chứng:** Tạo bảng triage 12 warnings có severity, evidence và false positive.

**Câu hỏi:** Mọi warning đều là finding?

<details><summary>Giải thích</summary>

Không, cần điều kiện và kiểm chứng.

</details>

---

## 06.07 · Foundry: stateful fuzz và invariant

**Phân tích chuyên sâu:** Dùng forge unit/fuzz/invariant test, handler, nhiều actor, chuỗi gọi hàm và replay counterexample; xác định scope invariant đúng.

**So sánh/chuyển đổi:** Stateful fuzz trên EVM không tự kiểm chứng privilege/owner của SVM.

**Bài thực hành có bằng chứng:** Viết invariant: sau borrow/withdraw được chấp thuận thì account phải đạt giới hạn nợ.

**Câu hỏi:** Happy path có chứng minh an toàn mọi chuỗi gọi?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.08 · Echidna & Medusa campaigns

**Phân tích chuyên sâu:** Thiết kế property-based fuzzing, seed, coverage, input generators, state sequences, corpus reduction và reproducible counterexamples.

**So sánh/chuyển đổi:** Các fuzzer này tập trung EVM, không trực tiếp chạy program SBF.

**Bài thực hành có bằng chứng:** Thiết kế 3 campaign: authority, accounting, oracle/rounding.

**Câu hỏi:** Fuzzer đảm bảo đã khám phá hết mọi trạng thái?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.09 · Halmos, Certora và formal proofs

**Phân tích chuyên sâu:** Formal verification kiểm chứng property dưới assumptions, bounds, model; ghi rõ chứng minh gì và không chứng minh gì.

**So sánh/chuyển đổi:** Một proof EVM không mặc nhiên chuyển sang SVM.

**Bài thực hành có bằng chứng:** Viết 3 bất biến có precondition rồi liệt kê assumptions, trạng thái chưa bao phủ.

**Câu hỏi:** Prover PASS nghĩa là protocol vô điều kiện an toàn?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.10 · Kế toán kinh tế: assets, liabilities, flows

**Phân tích chuyên sâu:** Lập value-flow graph, net assets, obligations, LP shares, fee, bad debt, custody và đơn vị tài sản; tránh đồng nhất TVL với solvency.

**So sánh/chuyển đổi:** Sai logic accounting nguy hiểm dù không có reentrancy.

**Bài thực hành có bằng chứng:** Tạo sổ cái giả 4 tác nhân qua 5 giao dịch và đối chiếu tài sản/nợ.

**Câu hỏi:** TVL cao có đủ để kết luận protocol solvent?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.11 · AMM: reserve, swap, fee, rounding

**Phân tích chuyên sâu:** Nắm x*y=k như AMM mẫu, invariant có phí, decimals, LP mint/burn, fee-on-transfer, rebasing, donation và rounding.

**So sánh/chuyển đổi:** Không dùng k cố định chính xác cho mọi AMM hoặc mọi thời điểm.

**Bài thực hành có bằng chứng:** Kiểm tra 6 tình huống swap và LP dưới rounding bằng test độc lập.

**Câu hỏi:** Có phí thì x*y luôn bằng đúng k ban đầu?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.12 · Oracle, collateral và liquidation stress

**Phân tích chuyên sâu:** Đánh giá stale data, decimals, TWAP, nguồn giá, liquidation discount, bad debt, thị trường cạn thanh khoản. Phân biệt healthy khi thao tác với giá biến động sau đó.

**So sánh/chuyển đổi:** Một khoản vay có thể trở nên undercollateralized khi thị trường giảm giá.

**Bài thực hành có bằng chứng:** Mô phỏng price shock 20/50%, nguồn giá 0/stale và khả năng liquidate.

**Câu hỏi:** Tất cả borrower luôn healthy ngay cả sau cú sốc giá?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.13 · MEV, transaction ordering, flash liquidity

**Phân tích chuyên sâu:** Mô hình sandwich, backrun, flash loans ở mức rủi ro phòng thủ; tính giá trị sau phí, trượt giá, vốn và execution risk.

**So sánh/chuyển đổi:** EVM ordering và Solana scheduling không được coi giống hệt nhau.

**Bài thực hành có bằng chứng:** Mô phỏng toy AMM với 3 thứ tự giao dịch và xác định slippage protection.

**Câu hỏi:** Flash loan cho vay vô hạn và miễn hoàn trả?

<details><summary>Giải thích</summary>

Không; phải hoàn trả theo điều kiện ngay trong giao dịch.

</details>

---

## 06.14 · Tokenomics, game theory và incentives

**Phân tích chuyên sâu:** Mô hình payoff actor: LP, trader, admin, keeper, liquidator; tìm reward farming, self-trading, sai lệch incentives và governance capture.

**So sánh/chuyển đổi:** Code phát thưởng đúng chưa chắc khuyến khích hành vi tốt.

**Bài thực hành có bằng chứng:** Viết payoff matrix, tìm một cơ chế khuyến khích ngược và 2 phương án chỉnh.

**Câu hỏi:** Một protocol không lỗi code có thể gặp exploit kinh tế?

<details><summary>Giải thích</summary>

Có.

</details>

---

## 06.15 · Composability, bridge và emergent failures

**Phân tích chuyên sâu:** Phân tích graph qua AMM-lending-oracle-bridge, token đặc biệt, callback, reorg/finality, dependency và trạng thái đa giao thức.

**So sánh/chuyển đổi:** CPI và EVM CALL cần threat model theo từng runtime.

**Bài thực hành có bằng chứng:** Vẽ chuỗi tin cậy qua 4 thành phần, chỉ ra assumption ở mỗi ranh giới.

**Câu hỏi:** Audit một contract bảo đảm mọi tích hợp an toàn?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.16 · Solang/SVM Security: account-centric audit

**Phân tích chuyên sâu:** Kiểm signer=authority, owner, writable, PDA seeds, program ID CPI, mint, IDL account ordering, CU, storage migration, upgrade authority.

**So sánh/chuyển đổi:** Foundry/Slither/Echidna/Halmos/Certora nhắm EVM không tự kiểm định Solang SBF.

**Bài thực hành có bằng chứng:** Viết bảng 12 negative tests hoán đổi account/authority và coverage EVM vs SVM.

**Câu hỏi:** Fuzz bản Solidity EVM chứng minh SBF trên Solana không lỗi?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.17 · PoC có phép, báo cáo finding và fix review

**Phân tích chuyên sâu:** Chạy toy/fork được phép, giữ initial state và logs, tìm root cause, impact thực tế, severity, patch, regression, residual risk.

**So sánh/chuyển đổi:** Đừng nhầm severity dự báo với bằng chứng thiệt hại thực.

**Bài thực hành có bằng chứng:** Viết finding với precondition, step test trên sandbox, patch diff và re-test.

**Câu hỏi:** Có cần tấn công mainnet trái phép để chứng minh bug?

<details><summary>Giải thích</summary>

Không.

</details>

---

## 06.18 · Capstone: audit Lending Toy và peer review

**Phân tích chuyên sâu:** Làm quy trình 5 pha; lập mental model, threat model, economic invariant, reproducible Foundry test, fix regression, báo cáo và reviewer độc lập.

**So sánh/chuyển đổi:** Top 500 là mục tiêu phấn đấu, không là bảng xếp hạng chính thức hay chứng chỉ.

**Bài thực hành có bằng chứng:** Chạy test/audit/TrainingLending.t.sol, báo cáo 2 trang và được phản biện chéo.

**Câu hỏi:** Một lab chứng minh bạn đã thuộc top 500 thế giới?

<details><summary>Giải thích</summary>

Không, cần năng lực dài hạn với bằng chứng công khai.

</details>

---

## Gương điển hình để học hỏi

Danh sách [100 hồ sơ tham khảo](../auditors.html) giúp học cách đọc public findings, đối chiếu người nghiên cứu và luyện kỹ năng qua bài tập. **Mã EX không phải thứ hạng toàn cầu**. Mỗi hồ sơ có xác định nguồn, chủ đề và việc nên tự thực hành. Xem thêm [hướng dẫn đối chiếu](07-auditor-role-models.md).

## Chuyên đề và đồ án

- [Playbook hai tư duy, 5 giai đoạn](06-audit-workflow-playbook.md)
- [Bất biến kinh tế và stress test](06-economic-invariants.md)
- [Bộ công cụ EVM vs Solang/SVM](06-svm-audit-boundaries.md)
- [Mẫu báo cáo audit và fix review](06-finding-template.md)
- [Thang năng lực và lộ trình 12 tháng](06-skill-matrix.md)
- [Lending toy lab và bài test Foundry](../examples/audit/README.md)

**Chính sách:** Tất cả bài lab nằm trên môi trường toy/local/permitted testnet. Không thử tấn công giao thức thật khi chưa được phép.

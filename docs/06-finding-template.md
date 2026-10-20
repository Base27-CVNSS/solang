# Mẫu báo cáo Audit Finding và Fix Review

## 1. Metadata

- **ID** AUD-YYYY-NN · **Severity** Critical/High/Medium/Low/Info (có lý do).
- **Scope** SHA, files/lines, compiler/target, dependency versions, cluster và run config.
- **Status** Unverified hypothesis / confirmed sandbox / mitigated / fixed / accepted.
- **Evidence confidence** biết rõ preconditions và whether behavior exists on production.

## 2. Intended behavior

Đội dự án dự định hệ thống phải có thuộc tính gì? Viết invariant và giới hạn (always / end-transaction / only successful borrow/withdraw).

## 3. Failure mode và assumptions

Giả định ngầm nào không được kiểm tra? Ai điều khiển input? Có quyền, thanh khoản, capital, oracle, timestamp hay multisig prerequisite không?

## 4. Reproduction có kiểm soát

- Test trong môi trường toy, private testnet hoặc fork có ủy quyền.
- Ghi initial state → calls → expected → actual → logs → assertion.
- Tái chạy được bằng câu lệnh chính xác. Không cung cấp key thật.

## 5. Root cause và impact

Trỏ code range và logic vi phạm. Phân biệt **thiệt hại tối đa có thể theo state thực** với lời tuyên bố mất toàn bộ TVL. Đánh giá likelihood, required capabilities và các controls đang tồn tại. Findings chưa đủ điều kiện thì ghi rõ “hypothesis”.

## 6. Remediation + regression

Đề nghị code diff, test dương/âm, xác minh preserved invariants, replay đúng failing sequence. Fix review chỉ bao trùm bản vá và đường bị ảnh hưởng; không ngầm tuyên bố tái audit toàn bộ.

## Ví dụ finding từ bài lab toy

**Tên:** Withdraw cho phép để lại debt không có collateral.

**Trước:** deposit(100), borrow(100) → trạng thái healthy.

**Lỗi:** withdraw(100) trên bản buggy thành công mà không kiểm tra debt.

**Sau:** debt=100, collateral=0, vi phạm invariant “sau successful withdraw, borrower vẫn healthy”.

**Giới hạn:** ví dụ không thực hiện chuyển token/ETH; đây là lỗi accounting trên **mô hình giả**, không phản ánh mất tài sản thực.

**Patch:** re-check health sau khi giảm collateral, revert nếu invalid.

**Kiểm thử:** test/audit/TrainingLending.t.sol có testcase tái hiện và testcase patched từ chối.

**Lưu ý:** các file là code học tập, chỉ ghi test PASS khi đã chạy thực tế trên máy của bạn.

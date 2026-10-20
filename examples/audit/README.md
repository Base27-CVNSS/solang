# Lending Training Lab — PoC an toàn trên số dư mô phỏng

**Mọi thao tác là sổ cái toy, không có ETH/ERC20 hoặc giao dịch Mainnet.** Hợp đồng ở `examples/audit/TrainingLending.sol` minh họa lỗi có chủ ý: withdraw không kiểm tra lại `debt <= collateral * 150 / 100`.

## Cách chạy với Foundry (nếu đã cài)

```bash
forge --version
forge test --match-path test/audit/TrainingLending.t.sol -vv
```

Repo không có backend deploy, CI/Foundry runner được xác nhận; **chưa được chạy test bởi công cụ trong lần cập nhật này**.

## Ba testcase

- `test_ReproducesBugOnToyState`: bản buggy cho phép vay còn dư nợ nhưng rút sạch collateral. Assertion đòi *nhìn thấy vi phạm* nên test PASS là tái hiện lỗi.
- `test_PatchPreventsUnsafeWithdrawal`: gọi withdraw sau vay phải revert; collateral còn nguyên.
- `testFuzz_PatchedWithdrawalStaysHealthy`: fuzz deposit/debt/withdrawal bounded; nếu rút bị chặn thì không làm thay đổi collateral; state cuối luôn healthy.

## Bài nộp

1. Mô tả tiền điều kiện, invariant và root cause.
2. Lưu `forge test -vv` log, phiên bản compiler và hash commit.
3. Đính kèm patch diff, phân tích vì sao không gây liveness regression.
4. Phân biệt toy accounting với lending có token thật, oracle, liquidation, interest, bad debt, LP withdrawals.
5. Nhờ một reviewer thử bác bỏ các điều kiện giả định.

Bài lab không nên deploy trên mainnet; không gợi ý dùng như lending protocol thật.

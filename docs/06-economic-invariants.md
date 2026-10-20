# Bất biến kinh tế cho Smart Contract Auditor

## 1. Năm lớp tư duy số học

- **Accounting:** tài sản/nghĩa vụ, giao dịch vào/ra, lỗ đã ghi nhận, fee, phân phối interest/LP share.
- **Solvency:** nghĩa vụ có thể được thanh toán bằng tài sản sau khi tính market price, haircut, bad debt, rủi ro thanh khoản.
- **Authorization:** ai có quyền chuyển quyền sở hữu, chỉnh tham số, lấy giá, thay implementation.
- **Liveness:** có đường thanh lý/repay/withdraw an toàn trong trạng thái thị trường xấu? Cơ chế pause có gây khóa vĩnh viễn?
- **Incentives:** một actor tối ưu lợi ích riêng có thể lách budget thưởng, governance hoặc thanh lý không?

## 2. Bảng invariant — KHÔNG áp dụng máy móc

| Mô hình | Property tham khảo | Điều kiện phạm vi | Stress test cục bộ |
|---|---|---|---|
| Collateralized lending | borrow/withdraw thành công thì debt ≤ LTV×collateralValue | chỉ cuối thao tác này; oracle hợp lệ theo spec | borrow→withdraw, stale price, shock giá |
| Vault | tổng shares, asset, fee và yield hạch toán đúng | rounding, donation, rebasing, fee-bearing asset | deposits rất nhỏ và rất lớn |
| Constant-product AMM | reserve đáp ứng quy tắc swap có phí | x×y=k chỉ baseline; k có thể tăng do fee | swap với token thu phí giả |
| Flash loans | end-state vault nhận đủ principal + fee | phí/token behavior và model theo spec | failed repayment phải rollback |
| Reward/staking | claimable + paid không vượt budget theo thiết kế | vốn mới được nạp và thời gian streaming | wash/self-reward mô phỏng |
| Oracle | giá phải có source/decimals/freshness/confidence hợp lệ | cơ chế fallback có thể khác | stale, zero, outlier |
| Bridge | message/nonce apply một lần đúng chain origin | finality và reorg | duplicate proof; reversed order |
| Governance | threshold/quorum/voting window đúng snapshot | borrowed voting power; roles | vote snapshot timing |
| Solang SBF | signer khớp authority; PDA + program owner đúng | theo instruction, quyền ghi, IDL | account swap trên local validator |

## 3. Công thức có diễn giải

### A. Giá trị của vị thế (đơn vị USD, ví dụ)

```text
collateral_value = amount_token × oracle_price × collateral_weight
debt_value       = borrowed_amount × debt_price
healthy_for_borrow = debt_value <= collateral_value × max_LTV
```

**Không** khẳng định mọi vị thế phải “healthy” mãi mãi: giá có thể giảm sau khi borrow, dẫn tới tình trạng cần thanh lý. Kiểm định phải gắn chính xác vào transition mà đặc tả yêu cầu. Oracle decimals phải quy đổi nhất quán; số thực trong tài liệu cần chuyển thành fixed-point integer trong code.

### B. Hạch toán

```text
balance_end = balance_begin + recorded_inflows
             - recorded_outflows + net_earnings
             - realized_losses - paid_fees
```

Với fee-on-transfer token, recorded_inflow có thể khác số người dùng định gửi. Với rebasing token, balance có thể đổi không cần chuyển; cần điều chỉnh mô hình.

### C. MEV/flash liquidity

```text
profit_net = value_extracted - gas/priority_fees - slippage
             - funding_cost - liquidation_loss - execution_risk
```

Không có vốn miễn phí vô hạn. Flash loan thường phải hoàn trả và trả phí trong transaction; mọi lệnh giả lập chạy offline, không giao dịch mainnet.

## 4. Ma trận stress 4 chiều

- Giá: bình thường, biến động -20%, -50%, mất nguồn, sai decimals.
- Thanh khoản: đầy đủ, mỏng, trượt giá cao, đóng băng.
- Actor: chủ ví, LP, keeper, liquidator, multisig, attacker giả lập.
- Thời gian: đảo thứ tự, lặp transaction, oracle stale, timelock delay.

Mỗi trường hợp lưu: giá, định danh dữ liệu đầu, invariant kỳ vọng, actual, counterexample, mitigation.

## 5. Ba lỗi tư duy hay gặp

1. **TVL ≠ solvency:** con số tổng tài sản không phản ánh nghĩa vụ trả LP, bad debt, slippage.
2. **x×y=k không phải universal invariant** trên mọi AMM khi fee, concentrated liquidity hoặc token đặc biệt.
3. **Proof of property ≠ proof of system:** mô hình formal được giới hạn bởi giả định và coverage.

Đồ án: thiết lập một bảng cân đối cho 4 tác nhân, chọn một giả định giá sai, đưa ra chiến lược phòng thủ bằng oracle freshness, caps, TWAP và liquidation gates; chứng minh bằng test trên toy.

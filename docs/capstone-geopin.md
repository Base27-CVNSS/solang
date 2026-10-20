# Capstone: GeoPIN — xác thực dấu vết bản ghi GIS

**Mục tiêu:** MVP chứng minh một bản ghi địa lý có SHA-256 nhất định được ghi nhận tại thời điểm giao dịch; không tuyên bố blockchain tự bảo đảm GPS là thật.

## Kiến trúc

```text
GPS / người đo → metadata + GeoJSON → chuẩn hóa → SHA-256
                                           ↓
WebGIS / Wallet Devnet → instruction/IDL → Solang program
                                           ↓
                             record owner/hash/version/nonce
                                           ↓
Verifier: đọc dữ liệu gốc → tính lại hash → kiểm tra tx/state
```

## 4 sprint thực chiến

1. **Data:** JSON schema, canonicalization (tái lập), SHA256 test vectors và chính sách riêng tư tọa độ.
2. **On-chain:** record, owner, PDA derivation, versioning và check signer/owner, unit tests.
3. **Fullstack:** WebGIS, Wallet Adapter, RPC Devnet, simulation, confirmation và xác minh record.
4. **Audit:** negative tests, account substitution, benchmark CU, kiểm tra upgrade authority và báo cáo provenance.

## Invariants và cảnh báo

- Signer phải trùng authority. Xác minh account owner, PDA seeds, program ID, type, writable.
- Không cho phép sửa âm thầm: ghi phiên bản tiếp theo và có liên kết hash / lịch sử.
- Dữ liệu off-chain phải canonicalize; một byte khác nhau phải tạo kết quả kiểm chứng khác.
- Không ghi địa chỉ nhà riêng, lộ trình cá nhân hoặc dữ liệu GPS nhạy cảm trực tiếp lên chain trừ khi có cơ sở pháp lý và thiết kế phù hợp.
- Muốn dùng làm chứng cứ pháp lý cần chain of custody, nguồn dữ liệu đáng tin, thiết bị/nhân chứng và quy trình pháp luật.

**Bàn giao:** mã nguồn, test, IDL thật, binary/commit hash, metadata phiên bản, testnet signature, bản demo và threat model.

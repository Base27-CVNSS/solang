# 05 · Bảo mật và chuyên gia

Kiểm thử, tối ưu CU, upgrade và GeoPIN capstone

> Tài liệu giảng dạy tiếng Việt. Các đoạn mã cần biên dịch/kiểm tra theo phiên bản Solang đã cài. Dùng local validator hoặc Devnet, tuyệt đối không dùng khóa mainnet.

## 05.01 Account substitution và kiểm tra quyền

**Cần nắm:** Threat model gồm account giả, wrong owner, wrong PDA, wrong mint, signer không phải authority. Kiểm tra mỗi bất biến và không chỉ dựa trên annotation.

**Dành cho Dev Solidity/EVM:** Tư duy truy cập khác EVM vì AccountMeta từ client.

**Bài thực hành:** Viết 6 test với accounts giả hoặc đổi thứ tự.

**Câu hỏi tự kiểm tra:** @account tự động bảo đảm account owner hợp lệ?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 05.02 CPI, program ID và trust boundary

**Cần nắm:** Chỉ gọi program ID đã biết hoặc có cơ chế allowlist; bảo vệ invariants, không tin dữ liệu từ program chưa xác thực. Xem xét reentrancy và lifecycle CPI.

**Dành cho Dev Solidity/EVM:** Không chỉ áp mẫu reentrancy guard từ EVM.

**Bài thực hành:** Vẽ cây tấn công thay Token Program bằng program độc hại.

**Câu hỏi tự kiểm tra:** Có thể CPI đến program chưa xác thực?

<details><summary>Mở đáp án</summary>

Không nên.

</details>

---

## 05.03 Unit, integration và property testing

**Cần nắm:** Kiểm thử happy path, lỗi auth, overflow, PDA seeds, invalid owner, rollback, migration; fuzz input và nhiều trạng thái, test mỗi invariant.

**Dành cho Dev Solidity/EVM:** Không có một bộ unit test EVM nào tự bảo đảm target Solana.

**Bài thực hành:** Viết test matrix 10 trường hợp cho AuthorityCounter.

**Câu hỏi tự kiểm tra:** Một test thành công là đủ lên Mainnet?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 05.04 Compute Units và tối ưu dữ liệu

**Cần nắm:** Đo bằng simulation và so sánh cùng workload; uint64 thường hiệu quả hơn uint256 khi đủ range; tối ưu vòng lặp, serialization và account space.

**Dành cho Dev Solidity/EVM:** Không quy đổi gas thành CU bằng hằng số.

**Bài thực hành:** Benchmark 3 phương án và ghi unit consumption.

**Câu hỏi tự kiểm tra:** -O aggressive luôn giảm CU mọi trường hợp?

<details><summary>Mở đáp án</summary>

Không, cần benchmark.

</details>

---

## 05.05 Upgrade authority và quy trình vận hành

**Cần nắm:** Bảo vệ quyền upgrade bằng cơ chế phê duyệt; ghi binary hash, IDL, checklist rollout, migration và kế hoạch xử lý sự cố. Không xóa authority bốc đồng.

**Dành cho Dev Solidity/EVM:** Proxy EVM khác nâng cấp program trên Solana.

**Bài thực hành:** Tạo checklist release và rollback/migration.

**Câu hỏi tự kiểm tra:** Binary mới tự sửa storage layout cũ?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 05.06 Capstone GeoPIN GIS on-chain

**Cần nắm:** Xây MVP chứng thực hash GeoJSON trên Devnet, ký bằng ví thử, verify transaction và state, mô hình versioning, audit trail và quản lý quyền. Bảo vệ dữ liệu vị trí nhạy cảm.

**Dành cho Dev Solidity/EVM:** Hash và chữ ký bảo đảm phát hiện sửa đổi trong điều kiện phù hợp, không phải chứng cứ pháp lý tuyệt đối.

**Bài thực hành:** Nộp thiết kế, test matrix, MVP WebGIS, benchmark và báo cáo bảo mật.

```json
{
  "recordId": "geo-001",
  "version": 1,
  "geometryHash": "<SHA-256 sau canonicalization>",
  "ownerPubkey": "<Solana pubkey>",
  "sourceProof": "<nguồn kiểm chứng>"
}
// JSON bài toán, không phải IDL hay ABI thực.
```

**Câu hỏi tự kiểm tra:** On-chain hash đủ chứng minh số đo ban đầu trung thực?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

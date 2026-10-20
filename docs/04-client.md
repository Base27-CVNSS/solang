# 04 · Client và Fullstack

TypeScript, Borsh, AccountMeta, SPL, RPC và dApp

> Tài liệu giảng dạy tiếng Việt. Các đoạn mã cần biên dịch/kiểm tra theo phiên bản Solang đã cài. Dùng local validator hoặc Devnet, tuyệt đối không dùng khóa mainnet.

## 04.01 Client TypeScript và ví

**Cần nắm:** Frontend → wallet adapter → RPC → IDL → program. Dùng cluster rõ ràng, không nhúng private key và không hardcode secret.

**Dành cho Dev Solidity/EVM:** ethers.js ABI thông thường không tự tương tác được với target Solana.

**Bài thực hành:** Vẽ sơ đồ module frontend, RPC và wallet.

**Câu hỏi tự kiểm tra:** Biết Program ID là encode được mọi hàm?

<details><summary>Mở đáp án</summary>

Không, cần schema/IDL.

</details>

---

## 04.02 Borsh và discriminator

**Cần nắm:** Dữ liệu instruction thường được mã hóa theo quy ước Anchor-compatible IDL, discriminator thường 8 byte; đối chiếu output compiler/SDK version đang dùng. Không dùng 4-byte Ethereum selector.

**Dành cho Dev Solidity/EVM:** Keccak EVM ABI selector khác Anchor discriminator.

**Bài thực hành:** Kiểm tra bytes payload tạo từ IDL thực.

**Câu hỏi tự kiểm tra:** Có thể dùng ethers encodeFunctionData làm instruction Solana?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 04.03 AccountMeta và quyền trong client

**Cần nắm:** AccountMeta gồm pubkey, isSigner, isWritable. Thứ tự phải theo IDL; các account do người dùng cung cấp phải được xác minh ràng buộc.

**Dành cho Dev Solidity/EVM:** EVM contract storage tự tham chiếu, Solana yêu cầu account list.

**Bài thực hành:** Lập bảng metas từ IDL Flipper hoặc AuthorityCounter.

```typescript
// Pseudocode SDK: thay bằng schema thực từ IDL
const accountMetas = [
  { pubkey: dataAccount, isSigner: false, isWritable: true },
  { pubkey: adminAccount, isSigner: true, isWritable: false }
];
// Đây chỉ là mẫu minh họa, KHÔNG phải metas đầy đủ của Flipper!
```

**Câu hỏi tự kiểm tra:** isSigner=true tự ký transaction?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 04.04 Transaction, simulation và CU

**Cần nắm:** Dùng simulation để xem lỗi/log/unitsConsumed, đặt compute budget hợp lý và xác nhận sau gửi. Trạng thái có thể thay đổi giữa simulate và gửi thật.

**Dành cho Dev Solidity/EVM:** Gas price/limit EVM khác compute unit price/limit.

**Bài thực hành:** Ghi unitsConsumed và so sánh 3 trường hợp input.

**Câu hỏi tự kiểm tra:** simulate thành công bảo đảm broadcast thành công?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 04.05 SPL Token và account model

**Cần nắm:** SPL Token Program quản lý mint, token account, authority. Không triển khai ERC-20 contract tùy ý rồi nghĩ đó là token chuẩn Solana.

**Dành cho Dev Solidity/EVM:** ERC-20 bytecode không port trực tiếp sang SPL Token.

**Bài thực hành:** Vẽ flow transfer SPL trên Devnet và role signer.

**Câu hỏi tự kiểm tra:** Mỗi mint SPL cần triển khai program riêng?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

## 04.06 Xây dựng DApp xác thực bản ghi

**Cần nắm:** Tách nguồn dữ liệu địa lý, canonicalization, SHA-256, trạng thái trên chain và UI verifier. Transaction chứng minh một hash đã được ghi nhận, không chứng minh GPS gốc là thật.

**Dành cho Dev Solidity/EVM:** Blockchain chứng minh tính nhất quán sau ghi, không chứng minh sự thật ngoài đời.

**Bài thực hành:** Thiết kế form GeoJSON hash + verify state và transaction.

**Câu hỏi tự kiểm tra:** Hash on-chain tự chứng minh tọa độ là đúng?

<details><summary>Mở đáp án</summary>

Không.

</details>

---

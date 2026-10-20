# Red-Team Checklist — bảo vệ chương trình Solang/Solana

Đây là hướng dẫn phòng thủ và thiết kế bài test âm tính (negative testing). Không triển khai payload trên mainnet, không sử dụng khóa cá nhân hoặc tài sản người khác.

## Các ranh giới tin cậy

1. Frontend không đáng tin: mọi public key, tham số, account list đều có thể bị sửa.
2. Signature chứng minh khóa đã ký, **không tự chứng minh signer có quyền nghiệp vụ**.
3. `owner` của account cần đối chiếu đúng program được chấp thuận trước khi giải mã state.
4. CPI target/program ID phải được xác thực, không dùng program ID bất kỳ do client nhập.
5. PDA seeds, bump và authority record phải khớp với ràng buộc nghiệp vụ.
6. Dữ liệu JSON/hash từ API ngoài chain có thể sai/giả mạo dù transaction on-chain hợp lệ.
7. Upgrade authority có thể thay code, làm thay đổi semantics của state cũ.
8. Account data size/layout có thể phá vỡ migration; không quên versioning.

## 12 bài test âm tính

| ID | Kịch bản | Kết quả cần đạt |
|---|---|---|
| RT01 | Signer là người khác authority | Reject |
| RT02 | isSigner=true nhưng không có chữ ký hợp lệ | Reject |
| RT03 | Account data thuộc owner program khác | Reject |
| RT04 | PDA thay seed/nonce | Reject |
| RT05 | Writable bị hạ xuống false | Reject an toàn |
| RT06 | Đổi thứ tự accounts | Không được cập nhật sai state |
| RT07 | CPI program ID bị tráo | Reject |
| RT08 | Truyền token mint không đúng | Reject |
| RT09 | Input vượt giới hạn u64 | Reject/không overflow |
| RT10 | Giao dịch thất bại giữa nhiều instructions | Rollback state |
| RT11 | Version cũ đọc bằng schema mới | Reject hoặc migrate xác định |
| RT12 | Cùng record cập nhật hai lần cạnh tranh | Invariant phiên bản/nonce được bảo vệ |

## Mẫu invariant GeoPIN

`record.owner == signer.pubkey` trước khi sửa; `record.version` tăng đúng một; hash có độ dài/format xác định; record PDA suy từ namespace/owner/recordId; verifier đối chiếu dữ liệu nguồn và transaction. Khi cần chống replay, dùng nonce/version được kiểm tra bằng state, không chỉ timestamp từ frontend.

## Quy trình audit

- Ghi một test cho từng invariant và ranh giới tin cậy.
- Lưu compiler version, SDK version, chương trình/thư viện đã liên kết.
- Thực hiện fuzzing/property tests và kiểm tra thay đổi layout.
- Đánh giá quyền nâng cấp, chi phí CU, khả năng làm cạn account/lamports và rủi ro denial-of-service.
- Đọc runtime logs, không kết luận chỉ từ frontend success toast.
- Nhờ kiểm toán độc lập trước production khi quản lý token/tài sản quan trọng.

Tham khảo: https://solana.com/docs/programs · https://github.com/solana-foundation/program-examples

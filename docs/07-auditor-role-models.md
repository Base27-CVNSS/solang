# 100 gương điển hình trong Smart Contract Audit — hướng dẫn học tập

## Phạm vi và nguồn

Thư viện `auditors.html` gồm **100 hồ sơ riêng** được biên tập từ tệp HTML do người dùng cung cấp ngày 20/10/2026. Mã EX001..EX100 là **mã định danh, không phải thứ hạng năng lực**. Danh sách không phải thống kê toàn bộ kỹ sư audit thế giới và không dùng để suy ra “top 500 toàn cầu”.

**Nguồn công khai dùng đối chiếu một số tên/handle:**

- Code4rena All-time Leaderboard: https://code4rena.com/leaderboard?timeframe=All+time
- Immunefi Whitehat Leaderboard: https://immunefi.com/leaderboard/
- Trail of Bits (nhân sự công khai): https://trailofbits.com/team
- Cantina — bảng kết quả Blast, chỉ để đối chiếu một số handle: https://cantina.xyz/leaderboard/c90131b4-5c7c-4ebc-a1f3-8002d219bfe0

Cùng một researcher có thể dùng nhiều bí danh; **không khẳng định hai handle là cùng một người nếu không có bằng chứng độc lập**. Tên xuất hiện trên leaderboard xác minh sự hiện diện của định danh; không xác minh đầy đủ thu nhập, tiểu sử, công việc hiện tại hoặc mọi thành tích nêu trong tài liệu tham khảo.

## Các mục được làm sạch

1. EX035: thay “Anurag Jain” (có nguy cơ đồng nhất với alias csanuragjain nhưng không xác định) bằng **nnez** đã xuất hiện trên Immunefi.
2. EX050: thay “Saw-Mon & Natalie” (hai cá nhân trong một hàng) bằng **bin2chen** trên Code4rena.
3. EX085: thay **CertiK**, là tên tổ chức, bằng **Bobface** trên Immunefi.
4. EX086: thay bản ghi **Tyler Diamond** bị lặp với EX047 bằng **MajorExcitement** trên Immunefi.

Mọi hồ sơ còn lại giữ chủ yếu tên/handle/thể loại gốc. Một số bí danh có thể che giấu danh tính thực hoặc không còn hoạt động; điều đó không thể xác minh chỉ bằng dữ liệu hiện có.

## Cách học thay vì chỉ đọc danh sách

- Nhóm **thi đấu:** xem cuộc audit công khai, phân tích invariant và dựng case test local mô phỏng đúng lỗi đã công bố.
- Nhóm **whitehat:** học disclosure có trách nhiệm, kiểm tra precondition và bằng chứng; không áp dụng exploit lên giao thức thật chưa được phép.
- Nhóm **công ty:** xem báo cáo audit công khai để học scope, mức rủi ro, root cause, patch và fix review.
- Nhóm **nghiên cứu:** tái tạo thí nghiệm trên chương trình mẫu, ghi giới hạn EVM/SVM, tránh nhầm kết quả tool thành chứng minh toàn giao thức.

## Kế hoạch 10 tuần

Mỗi tuần chọn 10 hồ sơ; chọn 1 finding hoặc nghiên cứu có nguồn xác minh để nộp **1 trang mô hình hệ thống, 1 invariant, 1 test đơn vị/fuzz, 1 khuyến nghị vá và 1 bản phản biện**. Sau 10 tuần phải có 10 study notes tái lập được, không chỉ hoàn thành 100 lần đánh dấu.

## Quy tắc đối chiếu

- Chỉ dùng tên/handle có link nguồn cấp nền tảng đã kiểm tra để đánh dấu **đã đối chiếu handle**.
- Số tiền thưởng, thứ hạng, chức danh trong phần **mô tả gốc (chưa kiểm chứng định lượng)** chỉ có giá trị ghi nhận tài liệu nguồn và cần kiểm tra lại trước khi phát hành.
- Không tự suy ra quốc tịch, giới tính, nhân thân, thông tin riêng tư hoặc đồng nhất alias.
- Đừng lấy chức vụ lãnh đạo công ty làm bằng chứng đứng đầu bảng cá nhân audit kỹ thuật.
- Cập nhật ngày và phạm vi xác minh khi sửa dữ liệu.

## Các gợi ý nâng cấp

Thêm nguồn cá nhân cụ thể, định danh bằng audit-report link/public GitHub hoặc contest page, review độc lập, feed lấy dữ liệu đã cấp phép và lịch sử kiểm chứng theo ngày; cần thực hiện bảo mật trước khi tự động hóa ingest.

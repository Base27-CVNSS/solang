# Giáo trình 07 — Phương trình Blockchain

**10 bài tiếng Việt** phân tích mô hình `B_A` từ định nghĩa, ma trận A, phát biểu và 7 định lý gốc cho đến 2 định lý bổ sung (elasticity và nghịch đảo/miền ảnh).

Đọc [Bản chứng minh 9 định lý](07-blockchain-equation-proofs.md), [Bộ kiểm thử và giới hạn](07-blockchain-equation-validation.md); thực hành qua [trang mô phỏng offline](../equation.html) và [Python không cần dependency](../examples/blockchain_equation.py).

**Phân biệt:** các định lý chứng minh tính chất của một mô hình được *định nghĩa*, không chứng minh A là chân lý về Bitcoin, Ethereum hay các blockchain khác. Những điểm M=0 hoặc M rất nhỏ theo mô hình có thể không tương ứng một mạng cụ thể ngoài đời. Số ví dụ Bitcoin/Ethereum là **giả định minh họa**.

## 07.01 Ký hiệu và định nghĩa cơ chế

**Kiến thức:** Chuẩn hóa M=(P,C,Delta,L), O=(I,V,R,T), miền [0,1]^4, ma trận A cố định. Phân biệt giá trị giả định với chỉ số đo.

**Liên hệ Dev/Audit:** Không nhầm mô hình blockchain với phương trình consensus runtime của Ethereum/Solana; đây là phép ánh xạ các chỉ số do người nghiên cứu chọn.

**Bài tập:** Đối chiếu mỗi hàng A với một phương trình thành phần; ghi lại giả định kinh tế/kiến trúc cần đo.

**Câu hỏi kiểm tra:** Ma trận A có được suy ra trực tiếp từ lịch sử block của Bitcoin?

<details><summary>Đáp án</summary>

Không; A là lựa chọn mô hình và cần kiểm định thực nghiệm.

</details>

---

## 07.02 Toán tử tích lũy thừa và 0^0

**Kiến thức:** Định nghĩa [M^B]_j=∏_i M_i^B_ij; đây không phải lũy thừa ma trận theo nghĩa đại số thông thường. Quy ước 0^0=1 chỉ cho exponent bằng 0.

**Liên hệ Dev/Audit:** Khi một biến cơ chế bằng 0, tính theo tích trực tiếp; không dùng log hay ma trận nhân thông thường.

**Bài tập:** Tính O tại M=(0,0.8,0.5,0.3) bằng tay.

**Câu hỏi kiểm tra:** 0^0 trong định nghĩa này được quy ước thành bao nhiêu?

<details><summary>Đáp án</summary>

1; do hàm nhân tử với số mũ 0 được định nghĩa hằng 1.

</details>

---

## 07.03 Định lý 1–2: xác định, liên tục, đơn điệu

**Kiến thức:** Với A cố định không âm, tích các hàm x^a xác định và liên tục trên [0,1], không giảm theo từng M_i nếu giữ các biến khác cố định.

**Liên hệ Dev/Audit:** Đơn điệu riêng phần không bảo đảm trilemma ngoài đời: thay đổi P có thể đồng thời làm Delta thay đổi.

**Bài tập:** Chứng minh ngắn và chạy 1000 phép thử tăng từng tọa độ, so sánh O trước/sau.

**Câu hỏi kiểm tra:** Tăng P ngoài thực tế chắc chắn không làm Delta giảm?

<details><summary>Đáp án</summary>

Không. Định lý chỉ nói về biến độc lập trong mô hình.

</details>

---

## 07.04 Định lý 3–4: sụp đổ biên và tính dương

**Kiến thức:** Mỗi cột A có ít nhất một số dương. M_i=0 ⇒ có O_j=0; mọi M_i>0 ⇒ mọi O_j>0.

**Liên hệ Dev/Audit:** Không suy ra một hệ thống tập trung không thể xác minh bằng chữ ký/Merkle proof; đây chỉ là đặc điểm A đã chọn.

**Bài tập:** Kiểm thử cả bốn phép gán P,C,Delta,L=0 trên mô phỏng.

**Câu hỏi kiểm tra:** Điều kiện mọi cơ chế dương có bảo đảm an ninh mạng blockchain thật?

<details><summary>Đáp án</summary>

Không, chỉ bảo đảm các đầu ra dương trong mô hình.

</details>

---

## 07.05 Định lý 5: dạng tích ↔ log tuyến tính ↔ mũ

**Kiến thức:** Với M>0, ln O=A ln M và O=exp(A ln M), theo từng tọa độ. Tại M_i=0, log không xác định và phải dùng dạng tích.

**Liên hệ Dev/Audit:** Không dùng tuyến tính log để suy ra A là nhân quả hay đã được ước lượng từ dữ liệu.

**Bài tập:** Đọc code tính forward, so kết quả trực tiếp với exp(A log M).

**Câu hỏi kiểm tra:** Có thể tính ln M_i khi M_i=0 không?

<details><summary>Đáp án</summary>

Không; phải tính dạng tích trực tiếp.

</details>

---

## 07.06 Định lý 6–7: tiêu chí nội sinh và Boolean AND

**Kiến thức:** Theo định nghĩa nội sinh “hợp lệ B ⇔ O dương”, M dương tương đương O dương. Khi mọi M là 0/1, full Boolean là AND của bốn cơ chế.

**Liên hệ Dev/Audit:** Một chain permissioned không bị loại khỏi ngành chỉ bởi ngưỡng do mô hình đề xuất.

**Bài tập:** Liệt kê 16 vector Boolean, xác nhận khi M toàn 1 thì O toàn 1.

**Câu hỏi kiểm tra:** Định lý 6 chứng minh tiêu chuẩn định nghĩa blockchain toàn cầu?

<details><summary>Đáp án</summary>

Không, tính hợp lệ ở đây là định nghĩa mô hình.

</details>

---

## 07.07 Định lý 8–9: elasticity, nghịch đảo và khả thi

**Kiến thức:** Với M>0: ∂ln O_j/∂ln M_i=a_ji. det A=-1, nên P=VT/I², C=V/R, Delta=I²R/(VT), L=T/I. Kiểm tra T≤I, V≤R, VT≤I², I²R≤VT.

**Liên hệ Dev/Audit:** Nghịch đảo cho phép chẩn đoán số liệu theo mô hình, không đo bản chất chain khi thiếu phương pháp lượng hóa.

**Bài tập:** Nhập O=(0.5,0.9,0.3,0.3) để thấy vi phạm V≤R; phục hồi M từ O hợp lệ.

**Câu hỏi kiểm tra:** Đầu ra V=0.9, R=0.3 có thể sinh bởi M trong [0,1]^4?

<details><summary>Đáp án</summary>

Không, vì C=V/R=3 >1.

</details>

---

## 07.08 Mô phỏng Bitcoin/Ethereum và lỗi số học

**Kiến thức:** Giữ các kịch bản trong bản thảo như ví dụ giả định. Ethereum giả định P=.75,C=1,Delta=.95,L=1 cho I=.95,V=.7125,R=.7125,T=.95 (không phải .90).

**Liên hệ Dev/Audit:** Không gán đây là phép đo Bitcoin hay Ethereum mới nhất nếu không có bằng chứng số liệu và định nghĩa chỉ số.

**Bài tập:** Chạy bốn kịch bản, so sánh kết quả, giải thích tác động L².

**Câu hỏi kiểm tra:** T của Ethereum ví dụ có bằng 0.90 không?

<details><summary>Đáp án</summary>

Không: C×Delta×L²=1×.95×1=.95.

</details>

---

## 07.09 Phản biện mô hình và validation khoa học

**Kiến thức:** A không độc nhất; P,C,Delta,L chưa định nghĩa cách đo, có khả năng trade-off, ngưỡng, tương tác, dữ liệu gốc sai, confirmation probabilistic và governance. Phải đánh giá giả thiết với dữ liệu độc lập.

**Liên hệ Dev/Audit:** Blockchain audit không được thay bằng điểm số mô hình; các phương trình không kiểm chứng bytecode hay quyền signer.

**Bài tập:** Viết 5 phản ví dụ thực nghiệm giả lập và kế hoạch đo, interval, alternative model.

**Câu hỏi kiểm tra:** Tính đúng của định lý toán chứng minh A phù hợp mọi chain?

<details><summary>Đáp án</summary>

Không, phải hiệu chuẩn và kiểm định A riêng.

</details>

---

## 07.10 Capstone: phương trình trong GeoChain và Audit

**Kiến thức:** Kết hợp mô phỏng phương trình với app GeoPIN: kiểm tra hash/GPS/provenance và an toàn blockchain qua quy trình độc lập. Đánh giá kết quả theo mức bất định, không tự xác nhận pháp lý.

**Liên hệ Dev/Audit:** Hash on-chain chứng minh dấu vết, không chứng minh sự thật GPS; chương trình Solang cần runtime audit riêng.

**Bài tập:** Nộp report 4 phần: định nghĩa chỉ số, 1000 property tests, 3 tình huống, 3 limitations và plan thực nghiệm.

**Câu hỏi kiểm tra:** Blockchain cho điểm I=T=1 có xác nhận hồ sơ đất đai chính xác?

<details><summary>Đáp án</summary>

Không, cần provenance, bên chứng thực và thủ tục pháp lý.

</details>

---

## Hoàn thành

Nộp chứng minh 7 định lý, tính được 5 kịch bản, kiểm thử nghịch đảo và điều kiện miền, trình bày ít nhất ba hạn chế thực nghiệm, có thể giải thích vì sao 'hợp lệ B' chỉ là tiêu chí nội sinh.

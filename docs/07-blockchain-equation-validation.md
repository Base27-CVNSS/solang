# Kiểm thử và phản biện Phương trình Blockchain

## Phân tầng luận điểm

- **Đã chứng minh trong mô hình đã chọn:** tính xác định, liên tục, đơn điệu theo từng biến độc lập, collapse ở biên, tính dương, tương đương log/mũ, điều kiện hợp lệ theo định nghĩa, Boolean special case, elasticity, và khả nghịch trong miền dương.
- **Chưa chứng minh:** ma trận A là độc nhất đúng/đúng nhân quả, chỉ số P,C,Δ,L có thang đo khách quan thống nhất, các giá trị ví dụ phản ánh mạng thật, phương trình là “bản chất của tất cả blockchain”.
- **Có thể kiểm định:** ràng buộc miền ảnh \(T\le I\), \(V\le R\), \(VT\le I^2\), \(I^2R\le VT\) khi thu thập dữ liệu chuẩn hóa đủ chất lượng; nếu bị vi phạm thì mô hình hoặc phép đo bị bác bỏ.

## Đặc tả property tests

**P1** Miền: inputs [0,1] luôn tạo outputs [0,1]; bỏ qua float rounding 1e-15.

**P2** Biên: đặt P=0 → V,R=0; C=0 → I,V,T=0; Δ=0 → mọi O=0; L=0 → I,T=0.

**P3** Đơn điệu: cố định 3 đầu vào, tăng đầu vào thứ 4, các đầu ra không giảm.

**P4** Boolean exhaustive: chạy \(2^4=16\) cấu hình, kiểm tra tích theo support matrix.

**P5** Log: với M>0, sai số giữa direct và \(\exp(A\ln M)\) nằm trong tolerance.

**P6** Nghịch đảo: với M>0 không quá sát zero, \(\mathrm{inverse}(\mathrm{forward}(M))≈M\).

**P7** Phản ví dụ miền: O với V>R phải bị đánh dấu inconsistent.

**P8** Ví dụ Ethereum bản thảo: \(T=0.95\), không phải 0.90.

**P9** Edge exponent: 0^0 được gán 1 khi số mũ bằng 0; không gọi log(0).

**P10** Nhạy sai số: gần-zero inverse có thể không ổn định; không kết luận lỗi network từ output gần zero của mô hình.

Chạy offline bằng Python (không cần thư viện ngoài):

\`\`\`bash
python3 examples/blockchain_equation.py --self-test
python3 tests/test_blockchain_equation.py
python3 examples/blockchain_equation.py 0.75 1 0.95 1
\`\`\`

## Rủi ro nghiên cứu

Định nghĩa “hợp lệ” tại \(\min(M)>0\) đủ để chứng minh (theo định nghĩa) mà không kiểm định hạ tầng. Tăng C ở một mạng có thể dẫn đến tăng thời gian xác nhận/giảm Δ; vì vậy **chỉ có đơn điệu riêng phần**, không phải hiệu quả hệ thống luôn tăng. Nếu đo một mạng có V>R, kiểm tra dữ liệu, đơn vị và sự khớp của định nghĩa trước khi bác bỏ A.

Khi học thuật hóa, cần đặc tả *measurement protocol*, sampling window, ground truth, và confidence intervals. Không gọi 4 số tùy chọn là “Bitcoin hiện tại/Ethereum hiện tại”.

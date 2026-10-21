# PHƯƠNG TRÌNH BLOCKCHAIN — Định nghĩa, phát biểu, 9 định lý và chứng minh

> **Phiên bản 1.0 · 21/10/2026 · Bài giảng mô hình toán học trong Solang Academy.** Giữ nguyên ma trận A và bảy định lý xuất phát từ bản thảo cung cấp, bổ sung định lý nghịch đảo, các điều kiện khả thi và kiểm tra số học. Đây là **mô hình đề xuất**, không phải định luật đã được thực nghiệm xác nhận cho mọi blockchain.

## 0. Khái niệm, thang đo và ký hiệu

Cho vector **cơ chế** (cột)

\[
\mathbf M=(P,C,\Delta,L)^\top\in[0,1]^4,
\]

trong đó **P** là mức phi tập trung; **C** là mức an toàn cơ chế mật mã; **Δ** là hiệu quả/độ tin cậy đồng thuận; **L** là mức tin cậy sổ cái phân tán, append-only.

Cho vector **thuộc tính**

\[
\mathbf O=(I,V,R,T)^\top\in[0,1]^4,
\]

trong đó **I** = khả năng chống sửa đổi theo định nghĩa mô hình; **V** = khả kiểm chứng; **R** = khả chống kiểm duyệt; **T** = khả truy xuất nguồn gốc. Các cụm từ này là **nhãn biến**, chưa phải chỉ số đo đã hiệu chuẩn.

Ma trận trọng số (hàng = thuộc tính, cột = cơ chế):

\[
A=\begin{pmatrix}0&1&1&1\\1&1&1&0\\1&0&1&0\\0&1&1&2\end{pmatrix}.
\]

Hệ số \(a_{44}=2\) không phải dữ liệu nhị phân, mà là **giả định mô hình** rằng T có độ nhạy mũ bằng 2 theo L.

### Định nghĩa toán tử thay vì lũy thừa ma trận chuẩn

Với \(M\in[0,1]^n\), \(B\in\mathbb R_{\ge0}^{n\times m}\), đặt

\[
[M^B]_j:=\prod_{i=1}^{n} M_i^{B_{ij}}\quad(j=1,\ldots,m).
\]

Đây là ký hiệu **tích lũy thừa từng phần tử** do ta tự định nghĩa, **không phải** phép lũy thừa ma trận thông thường trong đại số tuyến tính. Quy ước \(0^0=1\) khi exponent bằng 0. Cách viết "\(\mathbf A\circledast \mathbf M^{\mathbf A^\top}\)" trong bản gốc nên hiểu \(\circledast\) là ký hiệu nhắc phụ thuộc A, không phải phép Hadamard/matrix multiplication mới. Để tránh nhập nhằng, dùng **ký hiệu chính thống của bài học**:

\[
\boxed{\mathcal B_A(\mathbf M)=\mathbf M^{A^\top},\qquad
[\mathcal B_A(\mathbf M)]_j=\prod_{i=1}^4M_i^{a_{ji}}.}
\]

## 1. Ba dạng tương đương của phương trình

**Dạng trực tiếp:**

\[
\boxed{\begin{aligned}
I&=C\Delta L,\\
V&=PC\Delta,\\
R&=P\Delta,\\
T&=C\Delta L^2.
\end{aligned}}
\]

**Dạng log tuyến tính** (chỉ khi \(P,C,\Delta,L>0\)):

\[
\boxed{\ln\mathbf O=A\ln\mathbf M}
\]

**Dạng mũ:**

\[
\boxed{\mathbf O=\exp(A\ln \mathbf M)}
\]

Trong hai biểu thức cuối, log/exp áp dụng theo từng phần tử. **Không tính log khi có cơ chế bằng 0**: dùng dạng tích trực tiếp.

## 2. Định lý 1 — Tính xác định và liên tục

**Phát biểu.** \(\mathcal B_A:[0,1]^4\to[0,1]^4\) xác định và liên tục với quy ước \(0^0=1\).

**Chứng minh.** Với mỗi cặp \((j,i)\), số mũ \(a_{ji}\) bằng 0 hoặc là số dương. Nếu bằng 0, hàm nhân tử \(x^0\equiv1\) trên cả \([0,1]\), kể cả tại 0 nhờ quy ước. Nếu dương, \(x^{a_{ji}}\) liên tục trên \([0,1]\) và có giá trị từ 0 đến 1. Tích hữu hạn các hàm liên tục là liên tục và nằm trong \([0,1]\); mỗi thành phần \(O_j\) cũng vậy. \(\square\)

*Lưu ý:* Tính liên tục này đúng khi **A cố định**; nếu thay cả base và số mũ ở lân cận \(0^0\), tính liên tục hai biến không được bảo đảm.

## 3. Định lý 2 — Đơn điệu riêng phần

**Phát biểu.** Với A không âm và **giữ nguyên các biến còn lại**, \(O_j\) không giảm khi \(M_i\) tăng.

**Chứng minh.** Viết \(O_j=M_i^{a_{ji}}\cdot K\), với \(K=\prod_{k\neq i}M_k^{a_{jk}}\ge0\) không đổi. Hàm \(x\mapsto x^{a_{ji}}\) không giảm trên \([0,1]\) vì \(a_{ji}\ge0\). Nhân với hằng số không âm giữ tính không giảm. \(\square\)

**Giới hạn ngoại suy:** Trong thế giới thực \(P\) tăng có thể làm \(\Delta\) giảm, ví dụ trilemma hoặc chi phí liên lạc, nên **không thể** suy ra tăng phi tập trung thực tế không bao giờ làm giảm chỉ tiêu khác.

## 4. Định lý 3 — Sụp đổ ở biên

**Phát biểu.** Với A nêu trên, nếu một \(M_i=0\) thì **tồn tại ít nhất một** \(O_j=0\).

**Chứng minh.** Các cột A:

- P: \((0,1,1,0)^\top\). P=0 → V=0 và R=0.
- C: \((1,1,0,1)^\top\). C=0 → I=V=T=0.
- Δ: \((1,1,1,1)^\top\). Δ=0 → I=V=R=T=0.
- L: \((1,0,0,2)^\top\). L=0 → I=T=0.

Mỗi cột có một số mũ dương. Chọn hàng tương ứng j; tích có nhân tử \(0^{a_{ji}}=0\), nên \(O_j=0\). \(\square\)

**Đây là hệ quả cấu trúc của A, không phải một phát hiện rằng mọi hệ thống tập trung đều không thể kiểm chứng.** Một hệ thống tập trung có thể công bố chữ ký, Merkle proof và xác minh độc lập; lựa chọn V có P là một **giả định có thể bị phản biện**.

## 5. Định lý 4 — Điều kiện đủ cho tính dương

**Phát biểu.** Nếu \(\min_i M_i>0\), thì \(\min_jO_j>0\).

**Chứng minh.** Khi mỗi base dương, mọi \(M_i^{a_{ji}}>0\), kể cả số mũ 0. Tích hữu hạn của các số dương dương; vậy mọi thành phần O dương. \(\square\)

**Không được suy luận:** "Mọi cơ chế >0 ⇒ hệ thống đủ an toàn, đủ phi tập trung, hoặc thực sự là blockchain". Ví dụ \(P=10^{-12}\) vẫn >0 nhưng rất gần tập trung hoàn toàn.

## 6. Định lý 5 — Tương đương dạng tích, log và mũ

**Phát biểu.** Khi \(\mathbf M\in(0,1]^4\), ba công thức ở mục 1 tương đương.

**Chứng minh.** Từ dạng tích, lấy log: \(\ln O_j=\sum_i\ln(M_i^{a_{ji}})=\sum_i a_{ji}\ln M_i=(A\ln M)_j\). Ngược lại, lấy exp: \(O_j=\exp(\sum_i a_{ji}\ln M_i)=\prod_iM_i^{a_{ji}}\). Suy ra dạng mũ và log tương đương bằng exp/log thành phần. \(\square\)

## 7. Định lý 6 — Tiêu chí hợp lệ nội sinh (do định nghĩa)

**Định nghĩa nội sinh:** Gọi "hợp lệ theo mô hình B" khi **cả bốn thuộc tính O đều dương**, không gọi đây là định nghĩa toàn ngành.

**Phát biểu.** Ba mệnh đề tương đương:
(i) \(\min_i M_i>0\);
(ii) \(\min_j O_j>0\);
(iii) hợp lệ **theo định nghĩa mô hình B**.

**Chứng minh.** (i)→(ii) bởi định lý 4. (ii)→(i) bằng phản chứng: nếu có cơ chế zero, định lý 3 tạo một thuộc tính zero, mâu thuẫn. (ii)↔(iii) là định nghĩa được chọn, **không phải chứng minh được tính hợp lệ thực nghiệm của blockchain**. \(\square\)

## 8. Định lý 7 — Trường hợp Boolean

**Phát biểu.** Nếu \(M_i\in\{0,1\}\), thì \(O_j\in\{0,1\}\) và
\[
O_j=1 \iff M_i=1\text{ với mọi }i\text{ có }a_{ji}>0.
\]
**Chứng minh.** Khi base=1 mọi lũy thừa bằng 1; base=0 với số mũ dương cho 0; số mũ 0 cho 1. Tích các số Boolean bằng 1 khi và chỉ khi mọi nhân tử tương ứng số mũ dương bằng 1. \(\square\)

Do mọi cột A có ít nhất một hệ số dương, \(\min_j O_j=1\iff M_i=1\ \forall i\), tức phép hội AND bốn cơ chế **trong mô hình Boolean**.

## 9. Định lý 8 — Độ co giãn logarit (elasticity)

**Phát biểu.** Với \(M\in(0,1]^4\), từng cặp i,j có:
\[
\boxed{\frac{\partial\ln O_j}{\partial\ln M_i}=a_{ji}}.
\]
**Chứng minh.** Đạo hàm \(\ln O_j=\sum_k a_{jk}\ln M_k\) theo biến độc lập \(\ln M_i\) cho \(a_{ji}\). \(\square\)

**Hệ quả quan sát:** \(\partial\ln T/\partial\ln L=2\); tăng L 1% gần điểm nội miền sẽ làm T tăng xấp xỉ 2% **khi các cơ chế khác giữ nguyên**. Đây là mô tả **giả định số mũ 2**, chưa phải quan sát thực tế.

## 10. Định lý 9 — Khả nghịch, đồng nhất và chẩn đoán miền giá trị

Ta có:
\[
\det A=-1\ne0,\qquad
A^{-1}=\begin{pmatrix}
-2&1&0&1\\
0&1&-1&0\\
2&-1&1&-1\\
-1&0&0&1
\end{pmatrix}.
\]

**Phát biểu.** Trên \((0,1]^4\), phép \(\mathcal B_A\) là 1–1 trên ảnh của nó và nghịch đảo cho bởi:
\[
\boxed{
P=\frac{VT}{I^2},\quad
C=\frac VR,\quad
\Delta=\frac{I^2R}{VT},\quad
L=\frac TI.
}
\]

**Chứng minh.** \(\ln O=A\ln M\), vì A khả nghịch nên \(\ln M=A^{-1}\ln O\). Lấy exp từng hàng của nghịch đảo tạo ra bốn công thức trên. Tính nghịch đảo duy nhất với \(O_j>0\). \(\square\)

**Hệ quả có thể bác bỏ/kiểm tra (feasibility):** Khi chọn một \(\mathbf O\in(0,1]^4\) bất kỳ, để nó thực sự nằm trong ảnh từ \(\mathbf M\in(0,1]^4\), phải và đủ:
\[
T\le I,\quad V\le R,\quad VT\le I^2,\quad I^2R\le VT.
\]
Vì đây chính là điều kiện lần lượt \(L,C,P,\Delta\le1\) trong nghịch đảo; chiều ngược lại là thay các M phục hồi vào hàm B.

**Ví dụ chống nhầm lẫn:** Không thể đưa \((I,V,R,T)=(0.5,0.9,0.3,0.3)\) vào mô hình A như một quan sát nhất quán vì \(V>R\), đòi \(C=V/R=3>1\).

**Chú ý:** Công thức nghịch đảo không áp dụng trực tiếp tại các biên 0 và có thể nhạy sai số đo khi I,V,R,T gần 0. Một mô hình toán học có nghịch đảo không đồng nghĩa các chỉ số xã hội/đồng thuận ngoài đời đã được định lượng.

## 11. Các kịch bản số minh họa (không phải số đo thực địa)

| Kịch bản | P | C | Δ | L | I | V | R | T |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Lý tưởng Boolean | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| "Bitcoin" giả định | 0.85 | 1 | 1 | 1 | 1 | 0.85 | 0.85 | 1 |
| "Ethereum" giả định | 0.75 | 1 | 0.95 | 1 | 0.95 | 0.7125 | 0.7125 | **0.95** |
| CSDL tập trung có ký số | 0 | 0.8 | 0.5 | 0.3 | 0.12 | 0 | 0 | 0.036 |
| Không đồng thuận | 0.5 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |

Các giá trị 0.85 và 0.75 **là lựa chọn giả định từ bản thảo**, không phải phép đo phi tập trung Bitcoin/Ethereum được xác minh hay so sánh chuẩn hóa. \(T=0.90\) trong ví dụ Ethereum của bản thảo là **lỗi số học**, kết quả đúng là **0.95** với \(\Delta=0.95,L=1,C=1\).

## 12. Giới hạn khoa học, phản biện và nâng cấp

1. **A được chọn, không suy ra từ định lý hay dữ liệu.** Các định lý đúng cho hàm đã định nghĩa, không xác nhận các mối phụ thuộc là cơ chế thực của mọi chain.
2. **P,C,Δ,L chưa có định nghĩa thao tác/đơn vị đo.** Không dùng 0.8,0.95,... như số liệu thực nghiệm nếu thiếu phép đo và sai số.
3. **P=0 ⇒ V=0** chỉ đúng trong A, không đúng hiển nhiên trong thế giới thực. Verifiable database, Merkle proofs, signed logs có thể tồn tại dù quản trị tập trung.
4. **C,Δ,L không độc lập ngoài thực tế.** Nếu Δ=f(P) giảm, dấu hiệu toàn phần \(\mathrm d O/\mathrm dP\) có thể đảo, dù đạo hàm riêng dương.
5. **M_i>0 là ngưỡng toán học yếu.** Để đánh giá thực tế cần ngưỡng có chứng cứ và mô hình xác suất attack/censorship/finality.
6. **I không phải bất biến tuyệt đối.** Các chain có reorg, finality xác suất/kinh tế và rủi ro giả định mạng, cryptography và governance; có thể mô hình \(I(t)\) hoặc xác suất failure.
7. **Khả kiểm chứng, nguồn gốc thực tế không tự chứng minh tính đúng của dữ liệu gốc**: hash và blockchain chỉ phát hiện sai khác sau khi có bằng chứng neo, cần quy trình provenance cho GIS/đất đai.
8. **Định lý 6 một phần là định nghĩa**, không phải bằng chứng vĩ mô mọi blockchain đều là AND bốn cơ chế.
9. **Hồi quy log-log cần quan sát thực nghiệm** có biến thiên đủ rộng và nhận diện nhân quả; riêng dạng log-tuyến tính không tự làm mô hình được xác nhận.
10. **Cần phản ví dụ, so sánh mô hình cạnh tranh và confidence intervals** trước khi gọi là mô hình dự báo hay hệ tiên đề phổ quát.

### Mở rộng thực nghiệm hợp lệ

- Dữ liệu: cấu trúc validator, Nakamoto coefficient/HHI, chi phí tấn công, reorg probability và phân bố node.
- Đầu ra: thời gian finality, tỷ lệ giao dịch bị kiểm duyệt, khả năng xác minh từ light client, completeness của audit trail.
- Phù hợp hóa: học A từ dữ liệu có ràng buộc \(a_{ji}\ge0\) hoặc thêm tương tác, ngưỡng và biến ẩn; chạy out-of-sample.
- So sánh với NISTIR 8202 và tài liệu consensus thực của Bitcoin/Ethereum. Tài liệu NIST mô tả blockchain là ledger *tamper evident/tamper resistant*, thường không phụ thuộc trung tâm; Ethereum phân biệt finality kinh tế.

**Tài liệu nền:**

- [NIST Blockchain Technology Overview](https://www.nist.gov/publications/blockchain-technology-overview)
- [Ethereum Proof-of-Stake & Finality](https://ethereum.org/developers/docs/consensus-mechanisms/pos/)
- [Ethereum Proof-of-Stake FAQ](https://ethereum.org/developers/docs/consensus-mechanisms/pos/faqs/)
- [Solana Docs](https://solana.com/docs)

## 13. Bài toán kết hợp GIS / Audit

**GeoPIN / hash chứng thực:** Chỉ số L và C cao giúp tăng độ mạnh dấu vết giao dịch theo **giả định mô hình**, nhưng không suy ra GPS đúng. Chọn nguồn đo có thể chứng thực, hash canonical GeoJSON, giữ access logs, quản lý quyền và đối chiếu hash theo phiên bản.

**Audit Solidity và Solang:** Đừng dùng điểm mô hình B thay security audit. Bài học phù hợp để huấn luyện tư duy: viết assumptions → bất biến → phản ví dụ → mô phỏng → phân tích giới hạn.

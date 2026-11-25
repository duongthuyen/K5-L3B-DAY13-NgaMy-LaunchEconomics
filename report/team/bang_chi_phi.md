# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (tính tay: (1 − 0,2²) / 0,8 = 0,96 / 0,8) · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (tính tay: 1 / 0,8) · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (tính tay: (0,992 / 0,8) / 0,992) · ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi × 15 đ) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.805 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 / 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) / 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** hoá đơn chia số yêu cầu (4.472 / 274,7) [simulated]. Phần chênh là giờ nhân viên xem lại và làm lại.
- Khoản lớn nhất là **làm lại: 51,8%** tổng chi phí, sau đó là xem lại 40,7%. Token và tool cộng lại chỉ chiếm 7,5% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- Không đáng xử lý: **`quoc_te`**, đắt gấp 1,88× so với nhân viên tự làm [simulated]. Cho chạy lại tới 3 lần không giúp được, vì tỉ lệ lần chạy ok giảm dần 30,0% → 11,4% → 2,2% qua từng lần: lỗi nằm ở loại yêu cầu, không phải do may rủi.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi trong mẫu: 900 việc thành công trên 1.200 yêu cầu, chi phí biến đổi 3.414 đ mỗi việc thành công [simulated].

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

- Chi phí cố định **không đổi kết luận**: ở một nửa khối lượng vẫn chỉ 0,48× [simulated].
- Kết luận chỉ đảo khi khối lượng xuống dưới khoảng **6.200 yêu cầu/tháng** (40 tr / (12.000 − 3.414) ≈ 4.660 việc thành công, chia tỉ lệ 0,75).

## B1 · Đổi từng yếu tố

Gốc: 4.472 đ mỗi việc thành công [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

Tất cả số trong bảng là simulated. Đã kiểm: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của kịch bản "gấp đôi" tương ứng (token +251 / −126 đ; xem lại +1.820 / −910 đ; làm lại +2.315 / −1.157 đ).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng +5,6% + 40,7%, vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1% khi tăng 25%). Giá token chỉ +5,6% [simulated].

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = chi phí trợ lý + số yêu cầu không thành công × 12.000 đ (nhân viên làm thay).

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

Tất cả số trong bảng là simulated.

- Rẻ nhất cho công ty là **giới hạn 2 lần** (6,90 tr đ cả hệ thống) [simulated].
- **Không trùng** với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): chạy 1 lần nhìn rẻ nhưng đẩy thêm 85 ca cho nhân viên làm thay.

## B4 · Nếu phải xem lại tất cả

- Xem lại 100% (`noi_dia` + `hang_nang`, 982 yêu cầu): **11.743 đ = 0,98×** so với 12.000 đ theo 9 phút làm lại của đề; nếu dùng 15,3 phút làm lại từ dữ liệu thì 12.415 đ = 1,03× [simulated].
- Gần như hoà vốn, nên pilot phải đo được thời gian xem lại thật: trợ lý chỉ có lời khi mỗi lần xem lại ≤ 5,1 phút [simulated], và chỉ khi không phải xem lại mọi ca.

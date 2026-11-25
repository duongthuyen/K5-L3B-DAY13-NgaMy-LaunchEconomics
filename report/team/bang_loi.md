# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Hoàng Thị Thanh Nga (TV3) · Người gắn nhãn 2: Phương (TV4) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100% (≥ 80%, không cần viết lại định nghĩa). Nhãn bộ 2 lấy từ [nhan_bo_2_Phuong.md](nhan_bo_2_Phuong.md).

Phân bố nhãn (cả hai bộ giống nhau): Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng. Cả hai người đều phân vân ở ca 8, 9, 13 nên nhóm vẫn ghi quy tắc cho các ca dễ lệch, để dùng khi gắn nhãn ca mới:
- Ca 9 (mã sàn TMĐT) và ca 6 (chọn sai mục): nguyên nhân gốc là đầu vào sai của khách → **Do người dùng**; việc trợ lý không gợi ý là chỗ cần sửa, không phải nguyên nhân.
- Ca 13 (bảo hiểm đối tác): yêu cầu ngoài phạm vi → **Giới hạn hệ thống**; trả lời chung chung là cách thể hiện giới hạn kém.
- Ca 8 (dẫn điều 7.2 không tồn tại): trả lời sai so với chính sách và đã bị phát hiện → **Hệ thống**, không phải Ngầm.
- Ca 12, 17 (chỉ thấy khi kiểm tra/đối soát, không ai báo) → **Ngầm**; ca 2 có khách mở lại nên là **Hệ thống**.
- Ca 18 (tính đúng, khách hiểu sai vì thiếu cách tính) → **Ngữ cảnh**.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `ma_don_khong_hop_le` có `trace_id`; cảnh báo khi > 3% yêu cầu/ngày | Nhận diện mẫu mã đơn sàn TMĐT, hướng dẫn khách tìm mã vận đơn kèm ảnh minh hoạ | Product owner trợ lý |
| 7 | Hệ thống | Đối soát hằng giờ: số `hoan_tien_bao_thanh_cong` khớp bản ghi sổ cái theo `trace_id`; cảnh báo khi lệch ≥ 1 ca | Chỉ báo "thành công" khi sổ cái trả 2xx; lỗi 503 sau 3 lần → báo "đang xử lý" và chuyển nhân viên | Kỹ sư backend (tích hợp sổ cái) |
| 18 | Ngữ cảnh | Tỉ lệ `mo_lai_trong_7_ngay` có lý do "hoàn thiếu" trong khi số tiền đúng; ngưỡng > 1%/tuần | Mẫu tin nhắn luôn kèm cách tính (phí 30.000 đ × 50% = 15.000 đ) và điều khoản áp dụng | Người viết nội dung / UX writer |
| 11 | Giới hạn hệ thống | Event `dau_vao_khong_ho_tro` (loại = audio) đếm theo ngày; ngưỡng > 2% yêu cầu | Nói rõ chưa hỗ trợ thoại, chuyển nhân viên hoặc chuyển giọng nói thành chữ trước khi xử lý | Product owner trợ lý |
| 17 | Ngầm | Kiểm mẫu hằng ngày 50 đơn: so giá trợ lý dùng với bảng giá hiện hành; cảnh báo khi lệch ≥ 1 đơn | Xoá bộ nhớ đệm bảng giá khi có phiên bản mới; ghi `phien_ban_bang_gia` vào mỗi trace | Kỹ sư dữ liệu (quản lý bảng giá) |

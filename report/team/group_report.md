# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: NgaMy
- Lớp: L3B
- Thành viên: xem `TEAM.md` (Huyền, Tâm, Nga, Phương)

## 2. Mục tiêu và cách tiếp cận

Chuẩn bị hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có cho chạy pilot hay không. Cách tiếp cận: tính chi phí thật mỗi việc thành công từ trace (gồm cả giờ nhân viên xem lại và làm lại), tìm yếu tố nhạy nhất, phân loại lỗi, rồi thiết kế pilot có đối chứng và luật dừng viết trước. Mọi số từ cột `_simulated` ghi nhãn simulated.

## 3. Giải pháp

- **A · Mô hình chi phí** (`src/lab13.py`, [bang_chi_phi.md](bang_chi_phi.md)): tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `thanh_cong`; tách theo `loai`; cộng cố định 40 tr đ/tháng cho phạm vi noi_dia + hang_nang.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản đổi từng yếu tố, một cặp, giới hạn 1/2/3 lần chạy, xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md), [nhan_bo_2_Phuong.md](nhan_bo_2_Phuong.md)): hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, đồng thuận 20/20 = 100%, bảng khắc phục 5 loại.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu theo yêu cầu / nhân viên / depot trước khi chọn cách chia; chọn chia theo nhân viên 20 + 20.
- **E · Chỉ số, rủi ro, hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử + 2 tự đề xuất, 10 event có `trace_id`, 4 dòng rủi ro, hồ sơ 7 mục.

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token chia số yêu cầu [simulated].
- Ba yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%); giá token chỉ +5,6% [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× so với 12.000 đ [simulated] → thu hẹp phạm vi về noi_dia + hang_nang (0,38× sau cố định).
- Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6,90 tr đ), khác với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần) [simulated].
- Xem lại 100% gần hoà vốn: 0,98× [simulated].
- Pilot: 20 cụm mỗi nhóm, mde 6 điểm (đánh đổi đã ghi rõ), 4 luật dừng, quyết định 2027-01-08.
- **Đề xuất cuối của hồ sơ: Go có điều kiện** (4 điều kiện có người phụ trách và ngày kiểm tra).
- Kết quả duyệt chéo từ hội đồng: xem [phieu_cham.md](phieu_cham.md) (chưa có tại thời điểm viết báo cáo này).

## 5. Khó khăn và cách xử lý

- Chỉ có 40 nhân viên và 12 depot: không cách chia theo cụm nào đủ mẫu cho +5 điểm. Nhóm chấp nhận mde 6 điểm và ghi rõ power ≈ 0,64 nếu tác động thật là 5 điểm.
- Ngưỡng an toàn tuyệt đối 3% sẽ dừng pilot ngay tuần đầu vì tỉ lệ mở lại hiện đã 4,25%: chuyển sang ngưỡng so với đối chứng (+2 điểm) và trần 6%.
- Nhiều người cùng sửa file dễ trùng lấn: chia chủ file theo giờ trong `TEAM.md`, chỉ chủ file được sửa.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là giả lập; pilot phải đo thật qua event `staff_review_decision`, `staff_rework_completed`.
- Đợt chạy thử không có đối chứng, nên chỉ được nói "chỉ số trong đợt chạy thử là 82,83%", chưa kết luận tác động.
- Lỗi ngầm (ca 5, 12, 17) chỉ lộ qua kiểm tra mẫu; cần chỉ số kiểm tra mẫu hằng tuần như đề xuất trong `chi_so.md`.

## 8. Tài liệu tham khảo

- Đề bài `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, hướng dẫn `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/du_lieu_va_cong_thuc.md`.
- Google PAIR, People + AI Guidebook, chương "Errors + Graceful Failure".

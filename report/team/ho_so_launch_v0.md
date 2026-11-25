# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: NgaMy · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ mỗi việc thành công trên 1.200 yêu cầu [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8%, xem lại 40,7%, token + tool chỉ 7,5% ([bang_chi_phi.md](bang_chi_phi.md) A2) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại gấp đôi +51,8% · 2. Tỉ lệ xem lại gấp đôi +40,7% · 3. Lương nhân viên +25% → +23,1%; giá token gấp đôi chỉ +5,6% [simulated] (B1, B2) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi noi_dia + hang_nang: 3.414 đ biến đổi, cộng cố định 40 tr đ/tháng là 4.599 đ = 0,38× của 12.000 đ ở 45.000 yc/tháng, 0,48× ở một nửa khối lượng. **Bất lợi:** quoc_te 22.515 đ = 1,88× (loại khỏi phạm vi); nếu xem lại 100% thì 11.743 đ = 0,98× (1,03× với 15,3 phút làm lại) [simulated] (A3, A4, B4) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (đóng 24 giờ, không mở lại 7 ngày) · dùng 27,12% bỏ qua gợi ý · an toàn 4,25% mở lại 7 ngày; 10 event có `trace_id`. Không có đối chứng nên chưa kết luận tác động ([chi_so.md](chi_so.md) E1) | Giả lập | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, hai bộ nhãn độc lập; bộ 2 đã gửi ([nhan_bo_2_Phuong.md](nhan_bo_2_Phuong.md)): Hệ thống 5 · Do người dùng 4 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3. Tỉ lệ đồng thuận và bảng khắc phục 5 loại: chờ người gắn nhãn 1 ghép vào [bang_loi.md](bang_loi.md) | Chưa | Người gắn nhãn 1 (chủ `bang_loi.md`) |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot, 20 cụm mỗi nhóm; mde 6 điểm (859 hiệu dụng, ≥ 299 yêu cầu/người, DE 6,96); đánh đổi: power chỉ ≈ 0,64 nếu tác động thật +5 điểm; 4 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ; quyết định 2027-01-08 ([pilot_plan.yaml](pilot_plan.yaml)) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); xem lại 100% → 0,98×, hoà vốn khi xem lại ≤ 5,1 phút; lương +25% → 5.506 đ; khối lượng còn một nửa → 5.784 đ (0,48×) [simulated] ([chi_so.md](chi_so.md) E2) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** — chỉ cho chạy pilot (không phải chạy chính thức), phạm vi noi_dia + hang_nang (0,22× và 0,69×), loại quoc_te (1,88×) và doi_tac (0,85×). Con số bất lợi nhóm nêu rõ: xem lại 100% gần hoà vốn (0,98×), và với 40 nhân viên pilot chỉ thấy được chênh 6 điểm, không phải 5.

- Điều kiện 1: phút xem lại đo thật trung bình ≤ 5 phút/yêu cầu (hoà vốn 5,1 phút, simulated) ở cuối bước rollout 0.25 · Người phụ trách: PM trợ lý hoàn phí · Ngày kiểm tra: 2026-12-18.
- Điều kiện 2: tỉ lệ mở lại 7 ngày của nhóm trợ lý không cao hơn đối chứng từ 2 điểm và không vượt 6% (hiện 3,97% trong phạm vi), không có ca hoàn trùng tiền · Người phụ trách: Giám đốc vận hành LogiX-VN · Ngày kiểm tra: hằng tuần, lần đầu 2026-12-11.
- Điều kiện 3: chi phí mỗi việc thành công của nhóm trợ lý ≤ 8.000 đ (0,67×) hai tuần liên tiếp, tính từ event thật thay cho cột simulated · Người phụ trách: PM trợ lý hoàn phí · Ngày kiểm tra: 2026-12-25.
- Điều kiện 4: bảng lỗi đạt đồng thuận ≥ 16/20 và có khoá chống trùng (ca 20) + kiểm tra mã giảm giá (ca 5) trước ngày bắt đầu · Người phụ trách: Trưởng nhóm kỹ thuật trợ lý · Ngày kiểm tra: 2026-12-04.

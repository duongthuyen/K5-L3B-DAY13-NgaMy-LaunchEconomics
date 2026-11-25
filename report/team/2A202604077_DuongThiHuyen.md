# Báo cáo cá nhân — DuongThiHuyen-2A202604077

## 1. Thông tin thành viên

- Họ tên: Dương Thị Huyền
- MSSV: 2A202604077
- Email:
- Vai trong nhóm: người viết code (CP1–CP2), sau giải lao phụ trách `chi_so.md` (CP5)

## 2. Phần việc phụ trách

- `src/lab13.py`: phần CP1 (A1–A4) và CP2 (B1–B4).
- `report/team/chi_so.md`: E1 (đặc tả chỉ số, danh sách event) và E2 (rủi ro kinh tế).

## 3. Đóng góp cụ thể

- Viết ba hàm A1, qua ba phép thử 1,20 · 1,25 · 1,25; viết `mo_hinh` tính token và tool trên mọi lần chạy, kể cả lần lỗi, chia cho 978 việc thành công.
- A2: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu; làm lại chiếm 51,8% tổng chi phí [simulated].
- A3, A4: quoc_te 22.515 đ = 1,88× [simulated], lần thử 3 chỉ đúng 2,2% nên chạy lại không giúp; phạm vi noi_dia + hang_nang cộng cố định là 4.599 đ = 0,38× [simulated].
- B1–B4: làm lại gấp đôi +51,8%, xem lại gấp đôi +40,7%, lương +25% → +23,1%; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ); xem lại 100% là 11.743 đ = 0,98× [simulated].
- `chi_so.md`: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất, 10 event có `trace_id`, 4 dòng rủi ro kinh tế lấy số từ bảng độ nhạy.

## 4. Bằng chứng

- Commit `b43b0e3` (feat: CP1-CP2 trong lab13.py và chi_so.md); commit bổ sung bảng đối chiếu luật dừng của `pilot_plan.yaml` với event trong `chi_so.md`.
- Kiểm tra sau khi nhóm push đủ: `python lab13.py` chạy hết (A1 ĐẠT, D1 in đủ năm câu), `pilot_plan.yaml` hợp lệ và không còn `?`, `report/team` không còn từ cấm; số trong `ho_so_launch_v0.md` mục 1–4, 7 khớp output.
- Output `cd src && python lab13.py`: in "Ba phép thử đáp án biết trước: ĐẠT", bảng A2–A4, B1–B4 và ba chỉ số E1.
- File `src/lab13.py`, `report/team/chi_so.md`.

## 5. Công cụ AI đã dùng

- Claude Code: hỗ trợ viết code `mo_hinh`, các kịch bản B1–B4 và soạn khung `chi_so.md`.
- Tự kiểm tra: chạy `lab13.py`, đối chiếu từng số với bảng tự đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch dưới 2%); kiểm "giảm một nửa = nửa mức tăng của gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## 6. Tự đánh giá

- Hoàn thành đúng phần được giao, số khớp đáp án, mọi số từ cột `_simulated` có nhãn simulated.
- Cần cải thiện: tự tính tay thêm một con số A2 thay vì chỉ dựa vào output của code.

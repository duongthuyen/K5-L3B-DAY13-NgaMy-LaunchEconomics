# Báo cáo cá nhân — PhamMinhTam-2A202604097

## 1. Thông tin thành viên

- Họ tên: Phạm Minh Tâm
- MSSV: 2A202604097
- Email:minhtama11qc@gmail.com
- Vai trong nhóm: người kiểm số (CP1–CP2), sau giải lao là người viết code 2 (CP4, `pilot_plan.yaml`)

## 2. Phần việc phụ trách

- `report/team/bang_chi_phi.md`: kiểm số và điền phần A (A1–A4) và B (B1–B4).
- `src/lab13.py`: phần `TODO CP4` (D1, cỡ mẫu).
- `report/team/pilot_plan.yaml`: D1, D2, đánh đổi, luật dừng và mọi trường của kế hoạch pilot.

## 3. Đóng góp cụ thể

- A1: đối chiếu tay ba phép thử: (1 − 0,2²)/0,8 = 1,20; 1/0,8 = 1,25; (0,992/0,8)/0,992 = 1,25.
- A2: kiểm tổng 245.585 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585 đ; chia 978 việc thành công = 4.472 đ [simulated], gấp 16,3 lần hoá đơn 274,7 đ/yêu cầu.
- B1: kiểm "giảm một nửa = nửa mức tăng của gấp đôi" cho token (+251/−126 đ), xem lại (+1.820/−910 đ), làm lại (+2.315/−1.157 đ); B2 cộng tuyến tính 5,6% + 40,7% = 46,3% [simulated].
- A4: tính thêm ngưỡng đảo kết luận khi có chi phí cố định, khoảng 6.200 yêu cầu/tháng.
- D1: viết `co_mau` và `he_so_thiet_ke` trong `lab13.py`: 1.251 yêu cầu mỗi nhóm; m = 75 cần 84 người > 40; 20 người tối đa 1.000; 6 depot tối đa 300; mức chênh 6 điểm cần m ≥ 299 (DE 6,96).
- Đánh đổi: chọn chia theo nhân viên 20 + 20 với mức chênh 6 điểm; ghi rõ power chỉ còn ≈ 0,64 nếu tác động thật là 5 điểm, cần ≈ 10 ngày làm việc đo lường.
- `pilot_plan.yaml`: phạm vi `noi_dia` + `hang_nang` (dựa vào A3); ngưỡng an toàn so với đối chứng (+2 điểm) kèm trần 6%, vì tỉ lệ mở lại hiện tại đã là 4,25%; 4 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ (an toàn, chi phí, sử dụng, thời gian xem lại).

## 4. Bằng chứng

- Commit `33d367d` (docs: điền bang_chi_phi.md phần A và B).
- Commit `4ddece2` (feat: CP4 cỡ mẫu trong lab13.py và pilot_plan.yaml).
- Output `cd src && python lab13.py`: phần D1 in đủ năm câu a–e, power 0,64 và tỉ lệ mở lại 4,25% / 3,97%.
- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi; `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì.

## 5. Công cụ AI đã dùng

- Claude Code: đọc đề và `TEAM.md` để tóm tắt phần việc; chạy `lab13.py` và điền số vào `bang_chi_phi.md`; viết code `TODO CP4`; soạn `pilot_plan.yaml` và báo cáo này.
- Cách kiểm tra: tính tay lại A1, tổng A2 và quy tắc nửa/gấp đôi ở B1; đối chiếu năm câu D1 với số trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (1.251 · 3.103 · 1.000 · 300 · 299, khớp hoàn toàn); chạy hai lệnh kiểm YAML của CHECKPOINTS và `grep -rni production report/team`.
- Mọi số đều do `lab13.py` tính ra hoặc tính tay có ghi cách tính; không có số nào lấy từ AI mà không chạy code.

## 6. Tự đánh giá

- Hoàn thành đủ phần A, B (kiểm số) và D (code + YAML), push đúng hạn để TV3 kiểm tra chéo và TV4 điền hồ sơ.
- Điểm cần tự giải thích được trước hội đồng: vì sao chia theo cụm thì n hiệu dụng < c / ICC dù mỗi người làm bao nhiêu yêu cầu; vì sao chọn 20 + 20 nhân viên chứ không chia theo depot (6 cụm) hay theo yêu cầu (tràn tác động).
- Cần cải thiện: ngưỡng chi phí 8.000 đ và ngày quyết định do nhóm tự chọn, nên thống nhất với cả nhóm trước khi nộp.

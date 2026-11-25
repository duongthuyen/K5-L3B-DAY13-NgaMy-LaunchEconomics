# Báo cáo cá nhân — HoangThiThanhNga-2A202604079

## 1. Thông tin thành viên

- Họ tên: Hoàng Thị Thanh Nga
- MSSV: 2A202604079
- Email: hoangthanhnga2005@gmail.com
- Vai trong nhóm: người gắn nhãn 1, chủ `bang_loi.md` (CP3) → kiểm tra chéo và chủ trì `phieu_cham.md`

## 2. Phần việc phụ trách

- `report/team/bang_loi.md`: chép 20 ca, gắn nhãn bộ 1, ghép nhãn, tính đồng thuận, quy tắc phân biệt, bảng khắc phục 5 ca.
- Kiểm tra chéo trước khi nộp: chạy `lab13.py`, lệnh kiểm `pilot_plan.yaml`, `grep -rni production report/team`.
- `report/team/phieu_cham.md`: chủ trì chấm nhóm n + 1.

## 3. Đóng góp cụ thể

- Chép 20 ca từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` vào `bang_loi.md`. Gắn nhãn bộ 1 theo nguyên nhân gốc: Do người dùng 4 (ca 1, 6, 9, 14) · Hệ thống 5 (2, 7, 8, 15, 20) · Ngữ cảnh 4 (3, 10, 16, 18) · Giới hạn hệ thống 4 (4, 11, 13, 19) · Ngầm 3 (5, 12, 17).
- Ghép nhãn bộ 2 (TV4): trùng 20/20 = 100%.
- Viết trước quy tắc phân biệt cho các ca dễ lệch (6/9, 13, 8, 2 với 12/17, 18).
- Bảng khắc phục 5 ca đủ năm loại (9, 7, 18, 11, 17). Mỗi ca có event hoặc phép đối soát, ngưỡng và tần suất, và một vai phụ trách.
- Kết quả kiểm tra chéo (đã báo cho chủ file):
  - `lab13.py` ra ĐẠT và đủ các bảng A–E, D1. Máy mới phải `pip install statsmodels` trước, nếu không phần D1 lỗi `ModuleNotFoundError`. Nên ghi điều này vào `src/README.md`.
  - Trên Windows, `yaml.safe_load(open(...))` lỗi `UnicodeDecodeError` (cp1252). Chạy với `PYTHONUTF8=1` thì qua. Lệnh `grep '?'` không in gì.
  - `grep -rni production report/team` in đúng 1 dòng, trong `2A202604097_PhamMinhTam.md` dòng 36. Chữ này chỉ nằm trong tên lệnh, nhưng sẽ làm lệnh tự kiểm của CP5 không sạch. Đã báo TV2.

## 4. Bằng chứng

- File `report/team/bang_loi.md` (nhãn bộ 1, quy tắc, bảng khắc phục).
- Output `cd src && python lab13.py`: "Ba phép thử đáp án biết trước: ĐẠT"; E1 4,25% mở lại 7 ngày; D1 1.251 · 3.103 · 1.000 · 300 · 299.

## 5. Công cụ AI đã dùng

- Claude Code: trích văn bản 20 ca từ file .docx, soạn khung bảng và báo cáo, chạy các lệnh kiểm tra chéo.
- Cách kiểm tra: tự đọc lại từng ca với định nghĩa năm loại của Google PAIR trong đề. Bộ nhãn 2 do TV4 gắn độc lập, không lấy từ AI.

## 6. Tự đánh giá

- Xong phần khung, nhãn bộ 1, bảng khắc phục và kiểm tra chéo.
- Đã ghép nhãn bộ 2 của TV4: đồng thuận 20/20 = 100%.
- Còn chờ: hồ sơ của nhóm n + 1 để điền `phieu_cham.md`.

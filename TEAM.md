# Team

## Thông tin nhóm

- Tên nhóm: NgaMy
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-NgaMy-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/duongthuyen/K5-L3B-DAY13-NgaMy-LaunchEconomics · `main` · (điền hash commit chốt lúc nộp)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Dương Thị Huyền | 2A202604077 |       | duongthuyen | Người viết code 1 (CP1–CP2) → sau giải lao: phụ trách `chi_so.md` (CP5) |
|   2 | Tâm |      |       | | Người kiểm số (CP1–CP2) → sau giải lao: Người viết code 2 (CP4, `pilot_plan.yaml`) |
|   3 | Nga |      |       | | Người gắn nhãn 1, chủ `bang_loi.md` (CP3) → kiểm tra chéo & `phieu_cham.md` |
|   4 | Phương |      |       | | Người gắn nhãn 2, kiêm giữ hồ sơ `ho_so_launch_v0.md`, `group_report.md`, push bản chốt |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí (TV1 viết CP1–CP2, TV2 viết CP4).

## Phân công chi tiết

### Nguyên tắc chống trùng lấn

Mỗi file chỉ có **một người được sửa tại một thời điểm**. Người khác cần thay đổi thì nhắn cho chủ file, không tự sửa. Mỗi người commit/push ngay khi xong một phần và `git pull` trước khi bắt đầu phần mới.

| File | Chủ file | Thời gian được sửa |
| --- | --- | --- |
| `src/lab13.py` | TV1 → TV2 | TV1: 14:10–15:20 (`TODO CP1`, `TODO CP2`) · TV2: từ 15:35 (`TODO CP4`) |
| `report/team/bang_chi_phi.md` | TV2 | 14:10–15:20 |
| `report/team/bang_loi.md` | TV3 | Cả buổi |
| `report/team/pilot_plan.yaml` | TV2 | Từ 15:35 |
| `report/team/chi_so.md` | TV1 | Từ 15:35 |
| `report/team/ho_so_launch_v0.md` | TV4 | Cả buổi |
| `report/team/phieu_cham.md` | TV3 | 17:00–17:45 |
| `report/team/group_report.md` | TV4 | 17:45–18:00 |
| `TEAM.md` | TV4 | Mỗi người tự sửa **mục cá nhân của mình** lúc 17:45, lần lượt TV1 → TV2 → TV3 → TV4 (pull trước khi sửa) |
| `report/team/MSSV_HoTen_<từng người>.md` | Mỗi người một file riêng | 17:45–18:00, làm song song |

### TV1 — Huyền · Người viết code 1 → Chỉ số

| Giờ | Việc | Đầu ra |
| --- | --- | --- |
| 14:00–14:10 | Cài môi trường, chạy thử `lab13.py` | |
| 14:10–14:53 | CP1: viết ba hàm A1 (ĐẠT 1,20 · 1,25 · 1,25), `mo_hinh` (A2), gọi theo `loai` (A3), cộng cố định 40 tr đ/tháng (A4) | `src/lab13.py` in bảng A2–A4 → **push, báo TV2** |
| 14:53–15:20 | CP2: 9 kịch bản B1, B2, B3 (1/2/3 lần chạy), B4 (xem lại 100%) | `src/lab13.py` in bảng B → **push, báo TV2 & TV4**. Từ 15:20 **không sửa `lab13.py` nữa** |
| 15:35–16:36 | CP5-E1, E2: tính ba chỉ số (chính, dùng, an toàn), thêm 1 chỉ số dùng + 1 chỉ số an toàn, ≥ 6 event có `trace_id`, ≥ 2 dòng rủi ro kinh tế lấy số từ bảng B1 (do chính TV1 tính) | `report/team/chi_so.md` → push trước 16:40, **báo TV4** |
| 17:00–17:45 | Thuyết trình phần chi phí/độ nhạy trước hội đồng | |
| 17:45 | Báo cáo cá nhân, mục cá nhân trong `TEAM.md` | |

### TV2 — Tâm · Người kiểm số → Người viết code 2

| Giờ | Việc | Đầu ra |
| --- | --- | --- |
| 14:10–14:53 | Song song với TV1: tính tay A1 (1,20 · 1,25 · 1,25) và một con số A2 để đối chiếu; khi TV1 push thì điền bảng A2 (9 dòng, 2 dòng `simulated`), A3 (4 dòng), A4 và câu trả lời | `report/team/bang_chi_phi.md` (phần A) |
| 14:53–15:20 | Kiểm "giảm một nửa = nửa mức tăng của gấp đôi"; điền B1 (9 dòng), xếp hạng 3 yếu tố, trả lời B3, B4 (≤ 3 dòng, có số) | `report/team/bang_chi_phi.md` (phần B) → push, **báo TV1 & TV4** |
| 15:35–16:36 | CP4: pull `lab13.py`, viết `TODO CP4` (D1: cỡ mẫu theo yêu cầu / nhân viên / depot, mức chênh 6 điểm), trả lời D2, tính tỉ lệ `mo_lai_trong_7_ngay`, điền mọi `?`, ≥ 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ | `src/lab13.py`, `report/team/pilot_plan.yaml` → push trước 16:36, **báo TV3 & TV4** |
| 17:00–17:45 | Thuyết trình phần pilot trước hội đồng | |
| 17:45 | Báo cáo cá nhân, mục cá nhân trong `TEAM.md` | |

### TV3 — Nga · Người gắn nhãn 1 → Kiểm tra chéo & hội đồng

| Giờ | Việc | Đầu ra |
| --- | --- | --- |
| 14:10–15:20 | Đọc `RUBRIC.md`, `CHECKPOINTS.md`, theo dõi điều kiện "Xong khi" của CP1/CP2 và nhắc nhóm; chép 20 ca lỗi từ `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` vào khung bảng của `bang_loi.md` (chưa gắn nhãn, **không xem nhãn tham khảo** trong docs); đọc định nghĩa 5 loại lỗi Google PAIR | Khung `report/team/bang_loi.md` |
| 15:35–15:43 | Gắn nhãn độc lập 20 ca (ngồi tách TV4, không trao đổi) | Nhãn bộ 1 |
| 15:43–16:08 | Nhận nhãn bộ 2 từ TV4 (giấy/tin nhắn), ghép cả hai bộ vào file, tính đồng thuận (≥ 16/20), thống nhất ca lệch + ghi quy tắc, bảng khắc phục 5 ca đủ 5 loại (cách phát hiện đo được + vai phụ trách) | `report/team/bang_loi.md` → push, **báo TV4** |
| 16:08–16:55 | Kiểm tra chéo: clone sạch & chạy `cd src && python lab13.py` trên máy mình (ĐẠT), chạy lệnh kiểm `pilot_plan.yaml` của CP4, `grep -rni production report/team`; báo lỗi cho chủ file (không tự sửa) | Danh sách lỗi gửi chủ file |
| 17:00–17:45 | Chủ trì chấm nhóm n + 1 | `report/team/phieu_cham.md` → push |
| 17:45 | Báo cáo cá nhân, mục cá nhân trong `TEAM.md` | |

### TV4 — Phương · Người gắn nhãn 2, giữ hồ sơ, chốt nộp

| Giờ | Việc | Đầu ra |
| --- | --- | --- |
| 14:10–15:20 | Dựng khung 7 mục `ho_so_launch_v0.md`; điền số A/B ngay khi TV2 push `bang_chi_phi.md` (trạng thái + vai phụ trách từng mục); đọc định nghĩa 5 loại lỗi Google PAIR | `report/team/ho_so_launch_v0.md` (mục chi phí) |
| 15:35–15:43 | Gắn nhãn độc lập 20 ca (ngồi tách TV3), xong **gửi ngay cho TV3**, không sửa `bang_loi.md` | Nhãn bộ 2 |
| 15:43–16:55 | Điền dần hồ sơ: mục lỗi (sau khi TV3 push ~16:08), mục pilot (sau khi TV2 push ~16:36), mục chỉ số/rủi ro (sau khi TV1 push ~16:40); dòng cuối: Go / Go có điều kiện / No-go có lý do bằng số | `report/team/ho_so_launch_v0.md` đủ 7 mục **trước 17:00** |
| 17:00–17:45 | Gửi hồ sơ cho hội đồng, trả lời câu hỏi về đề xuất | |
| 17:45–18:00 | `group_report.md`; mục cá nhân trong `TEAM.md` (sau TV3); kiểm checklist `SUBMISSION.md`, điền hash commit chốt, push bản cuối | `report/team/group_report.md`, `TEAM.md` |

### Flow phụ thuộc (việc nào phải chờ)

```text
CP1/CP2:  TV1 push lab13.py (A ~14:50, B ~15:15) ──► TV2 điền bang_chi_phi.md ──► TV4 chép số vào hồ sơ
          (TV2 tính tay A1/A2 và TV3 chép 20 ca chạy song song, không chờ ai)

CP3:      TV3 + TV4 gắn nhãn song song, độc lập ──► TV4 gửi nhãn cho TV3 ──► TV3 ghép, tính đồng thuận, bảng khắc phục ──► TV4 điền mục lỗi

CP4/CP5:  TV1 dừng sửa lab13.py lúc 15:20 ──► TV2 viết TODO CP4 + pilot_plan.yaml ──► TV3 kiểm tra ──► TV4 điền mục pilot
          TV1 viết chi_so.md (dùng số B1 của chính mình, không chờ ai)  ──► TV4 điền mục chỉ số/rủi ro
          Tất cả ──► TV4 chốt hồ sơ trước 17:00

Nộp:      Báo cáo cá nhân song song · mục cá nhân TEAM.md lần lượt TV1 → TV2 → TV3 → TV4 · TV4 push bản chốt
```

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## DuongThiHuyen-2A202604077

### Phần việc phụ trách

- `src/lab13.py` phần CP1 (A1–A4) và CP2 (B1–B4); `report/team/chi_so.md` (E1, E2)

### Đóng góp cụ thể

- Viết ba hàm A1 (ĐẠT 1,20 · 1,25 · 1,25) và `mo_hinh`; A2 ra chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn chia số yêu cầu.
- In A3 theo loại (quoc_te 1,88×, không đáng xử lý), A4 cộng cố định (4.599 đ = 0,38× ở 45.000 yc/tháng), B1–B4 (làm lại gấp đôi +51,8%; giới hạn 2 lần rẻ nhất cho cả hệ thống; xem lại 100% = 0,98×).
- Viết `chi_so.md`: ba chỉ số tính thử (82,83% · 27,12% · 4,25%), hai chỉ số tự đề xuất, 10 event có `trace_id`, 4 dòng rủi ro kinh tế.

### Bằng chứng

- Output `cd src && python lab13.py`; các commit sửa `src/lab13.py` và `report/team/chi_so.md`.

## Tâm-MSSV

### Phần việc phụ trách

- `report/team/bang_chi_phi.md` (kiểm số A, B); `src/lab13.py` phần CP4 (D1); `report/team/pilot_plan.yaml`

### Đóng góp cụ thể

-

### Bằng chứng

-

## Nga-MSSV

### Phần việc phụ trách

- `report/team/bang_loi.md` (nhãn bộ 1, đồng thuận, bảng khắc phục); kiểm tra chéo trước nộp; `report/team/phieu_cham.md`

### Đóng góp cụ thể

-

### Bằng chứng

-

## Phương-MSSV

### Phần việc phụ trách

- Nhãn bộ 2 ở CP3; `report/team/ho_so_launch_v0.md`; `report/team/group_report.md`; chốt `TEAM.md` và push bản nộp

### Đóng góp cụ thể

-

### Bằng chứng

-

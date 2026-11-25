# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Người phụ trách file: Huyền (người viết code 1). Số tính bằng `src/lab13.py` (mục E1 cuối output) trên 1.200 yêu cầu của đợt chạy thử; dữ liệu giả lập.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu ở nhóm can thiệp được nhân viên mở bằng trợ lý | Số `agent_suggestion_shown` có `arm = can_thiep`, chia số `refund_request_created` có `arm = can_thiep` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | Số `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung`, chia số đơn được kiểm tra mẫu trong tuần | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%; không viết "trợ lý đã nâng chỉ số từ 0,70" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi bấm gửi / sửa / bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason, tom_tat, so_lan_chay, trace_id | Khi chuyển nhân viên sau lần chạy cuối |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi đóng ticket |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại ticket |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính.

- Chính: `ticket_closed` (closed_at − created_at ≤ 24 giờ) và không có `ticket_reopened` trong 7 ngày, chia số `refund_request_created`.
- Dùng (bỏ qua gợi ý): `staff_review_decision` có quyet_dinh là sua hoặc bo, chia tổng số `staff_review_decision`.
- An toàn (lọt đến khách): số `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia số `refund_request_created`.
- Dùng (đề xuất): `agent_suggestion_shown` chia `refund_request_created`, cùng lọc arm = can_thiep.
- An toàn (đề xuất): `audit_sample_checked` có so_tien_da_hoan ≠ so_tien_dung, đối chiếu với `refund_ledger_write` qua trace_id.
- Chi phí mỗi việc thành công (dùng cho rủi ro E2): `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút thật thay cho cột simulated), chia số ticket đóng không mở lại.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy và A4 (`src/lab13.py`, `bang_chi_phi.md`); mọi tác động đều **simulated**.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi noi_dia + hang_nang) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Tỉ lệ xem lại không giảm được, phải xem lại 100% | 11.743 đ = 0,98× của 12.000 đ (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated]; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút | % yêu cầu được xem lại còn > 50% ở cuối bước 0.25; phút xem lại đo thật trung bình > 5 phút | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ [simulated] | Đơn giá phút nhân viên trong bảng lương quý mới > 2.400 đ | Cập nhật mô hình, ưu tiên giảm phút xem lại trước khi mở rộng | PM trợ lý hoàn phí |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yc/tháng (4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |

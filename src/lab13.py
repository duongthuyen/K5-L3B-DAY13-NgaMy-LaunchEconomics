"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000  # chi phí cố định của trợ lý, đồng/tháng
YC_THANG = 45_000           # yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn; yêu cầu vượt coi là chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
                so_yc=len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps là simulated)')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f'Số lần gọi tool: {runs["tool_calls"].sum():,} · phút xem lại {reqs["phut_xem_lai_simulated"].sum():,} '
          f'· phút làm lại {reqs["phut_lam_lai_simulated"].sum():,} [simulated]')
    print(f'CPS gấp {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} lần hoá đơn chia số yêu cầu; '
          f'làm lại {ket_qua["lam_lai"] / ket_qua["tong"]:.1%}, xem lại {ket_qua["xem_lai"] / ket_qua["tong"]:.1%} '
          f'tổng chi phí [simulated]')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay): {he_thong_moi_yc:,.0f} đ '
          f'= {he_thong_moi_yc / BASELINE:.2f}× của {BASELINE:,} đ [simulated]')

    # ---------- CP1 · Nhiệm vụ A3: tách theo loại ----------
    print('\nA3 · Theo loại yêu cầu [simulated]')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>8s} {"x12000":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        con = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, con)
        print(f'{loai:10s} {len(con):6d} {r["thanh_cong"] / len(con):9.1%} '
              f'{con["so_lan_chay"].mean():7.2f} {r["cps"]:8,.0f} {r["cps"] / BASELINE:6.2f}×')
    ok_theo_lan = (runs.merge(reqs[['request_id', 'loai']])
                   .assign(ok=lambda d: d['status'] == 'ok')
                   .pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean'))
    print('Tỉ lệ lần chạy ok theo lần thử (attempt):')
    print(ok_theo_lan.round(3).to_string())

    # ---------- CP1 · Nhiệm vụ A4: chi phí cố định, phạm vi noi_dia + hang_nang ----------
    pham_vi = reqs[reqs['loai'].isin(PHAM_VI)]
    r_pv = mo_hinh(runs, pham_vi)
    print(f'\nA4 · Phạm vi noi_dia + hang_nang: {r_pv["thanh_cong"]} việc thành công / {len(reqs)} yc của mẫu, '
          f'tổng {r_pv["tong"]:,.0f} đ, CPS {r_pv["cps"]:,.0f} đ [simulated]')
    for ten, he_so in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        viec_thang = YC_THANG * he_so * r_pv['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / viec_thang
        tong_viec = r_pv['cps'] + co_dinh
        print(f'{ten:20s} {viec_thang:8,.0f} việc/tháng  cố định {co_dinh:6,.0f} đ/việc  '
              f'CPS + cố định {tong_viec:6,.0f} đ = {tong_viec / BASELINE:.2f}× [simulated]')

    # ---------- CP2 · Nhiệm vụ B1: đổi từng yếu tố ----------
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    print(f'\nB1 · Độ nhạy [simulated] (gốc {goc:,.0f} đ)')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # ---------- CP2 · Nhiệm vụ B2: đổi một cặp ----------
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) [simulated]')

    # ---------- CP2 · Nhiệm vụ B3: giới hạn chạy lại, chi phí cả hệ thống ----------
    print('\nB3 · Giới hạn chạy lại [simulated]')
    for k in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = r['so_yc'] - r['thanh_cong']
        he_thong = r['tong'] + khong_tc * BASELINE
        print(f'{k} lần: trợ lý {r["tong"]:11,.0f} đ  không thành công {khong_tc:4d}  '
              f'cả hệ thống {he_thong:11,.0f} đ  CPS {r["cps"]:6,.0f} đ')

    # ---------- CP2 · Nhiệm vụ B4: xem lại 100% trong phạm vi noi_dia + hang_nang ----------
    PHUT_XEM, PHUT_LAM_DE = 5, 9
    runs_pv = runs[runs['request_id'].isin(pham_vi['request_id'])]
    co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pham_vi['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
                     + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = int((pham_vi['ket_qua'] == 'thanh_cong').sum())
    phut_lam_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\nB4 · Xem lại 100% ({len(pham_vi)} yc, {co_ok} có lần chạy ok, {so_lam_lai} ca làm lại, '
          f'token + tool {token_tool_pv:,.0f} đ) [simulated]')
    for nhan, phut_lam in [('9 phút làm lại (đề)', PHUT_LAM_DE),
                           (f'{phut_lam_tb:.1f} phút làm lại (dữ liệu)', phut_lam_tb)]:
        tong_b4 = co_ok * PHUT_XEM * LUONG_PHUT + so_lam_lai * phut_lam * LUONG_PHUT + token_tool_pv
        cps_b4 = tong_b4 / tc_pv
        hoa_von = (BASELINE * tc_pv - token_tool_pv - so_lam_lai * phut_lam * LUONG_PHUT) / (co_ok * LUONG_PHUT)
        print(f'{nhan:28s} tổng {tong_b4:12,.0f} đ  CPS {cps_b4:7,.0f} đ = {cps_b4 / BASELINE:.2f}×  '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')

    # ---------- CP5 · Nhiệm vụ E1: tính thử ba chỉ số (phục vụ chi_so.md) ----------
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0))
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan = reqs['mo_lai_trong_7_ngay'] == 1
    lam_lai_pv_rate = (pham_vi['ket_qua'] == 'lam_lai').mean()
    print(f'\nE1 · Chính {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)}) · '
          f'Dùng (bỏ qua gợi ý) {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)}) · '
          f'An toàn (mở lại 7 ngày) {an_toan.mean():.2%} ({an_toan.sum()}/{len(reqs)}) · '
          f'Tỉ lệ làm lại trong phạm vi {lam_lai_pv_rate:.1%}')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower

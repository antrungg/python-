danh_sach_sp = [
    {"ma_sp": "SP01", "ten_sp": "Ao ", "gia": 150000, "ton_kho": 20},
    {"ma_sp": "SP02", "ten_sp": "Quan ", "gia": 350000, "ton_kho": 3},
    {"ma_sp": "SP03", "ten_sp": "Giay ", "gia": 500000, "ton_kho": 12},
    {"ma_sp": "SP04", "ten_sp": "Dep ", "gia": 80000, "ton_kho": 4},
]

lich_su_don_hang = []


def nhap_so_nguyen(loi_nhac):
    """Hàm nhập số nguyên dương an toàn bằng try-except"""
    while True:
        try:
            val = int(input(loi_nhac))
            if val > 0:
                return val
            print("-> Loi: Vui long nhap mot so nguyen duong!")
        except ValueError:
            print("-> Loi: Du lieu khong hop le, vui long nhap lai mot so nguyen.")


def tim_sp_theo_ma(ma_sp):
    for sp in danh_sach_sp:
        if sp["ma_sp"].upper() == ma_sp.upper():
            return sp
    return None


def hien_thi_danh_sach_sp():
    print("\n" + "=" * 65)
    print(
        f"{'Ma SP':<10}{'Ten San Pham':<20}{'Gia Ban':<15}{'Ton Kho':<10}{'Trang Thai':<10}"
    )
    print("-" * 65)
    if not danh_sach_sp:
        print("Cua hang chua co san pham nao.")
    else:
        for sp in danh_sach_sp:
            trang_thai = (
                "Sap het"
                if sp["ton_kho"] <= 5
                else ("Het hang" if sp["ton_kho"] == 0 else "Con hang")
            )
            print(
                f"{sp['ma_sp']:<10}{sp['ten_sp']:<20}{sp['gia']:>10,} VND{sp['ton_kho']:>10}  {trang_thai:<10}"
            )
    print("=" * 65)


def xem_sp_sap_het():
    sp_sap_het = [sp for sp in danh_sach_sp if sp["ton_kho"] <= 5]
    print("\n--- DANH SÁCH SẢN PHẨM SẮP HẾT HÀNG (<= 5) ---")
    if not sp_sap_het:
        print("Tất cả sản phẩm đều còn đủ hàng.")
        return
    for sp in sp_sap_het:
        print(
            f"Ma: {sp['ma_sp']} | Ten: {sp['ten_sp']} | Ton kho: {sp['ton_kho']} | Gia: {sp['gia']:,} VND"
        )


def them_san_pham():
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    ma_sp = input("Nhap ma san pham moi (vi du SP05): ").strip().upper()
    if tim_sp_theo_ma(ma_sp) is not None:
        print(f"-> Loi: Ma san pham {ma_sp} da ton tai!")
        return

    ten_sp = input("Nhap ten san pham: ").strip().title()
    gia = nhap_so_nguyen("Nhap gia ban (VND): ")
    ton_kho = nhap_so_nguyen("Nhap so luong nhap kho: ")

    sp_moi = {"ma_sp": ma_sp, "ten_sp": ten_sp, "gia": gia, "ton_kho": ton_kho}
    danh_sach_sp.append(sp_moi)
    print(f"-> Da them san pham {ten_sp} ({ma_sp}) vao kho thanh cong!")


def ban_hang():
    print("\n--- BÁN HÀNG / TẠO ĐƠN HÀNG ---")
    ma_sp = input("Nhap ma san pham can mua: ").strip().upper()
    sp = tim_sp_theo_ma(ma_sp)
    if sp is None:
        print(f"-> Loi: Khong tim thay san pham co ma {ma_sp}.")
        return

    if sp["ton_kho"] == 0:
        print(f"-> Loi: San pham {sp['ten_sp']} da het hang!")
        return

    print(
        f"San pham: {sp['ten_sp']} | Gia: {sp['gia']:,} VND | Ton kho: {sp['ton_kho']}"
    )
    so_luong_mua = nhap_so_nguyen("Nhap so luong can mua: ")

    if so_luong_mua > sp["ton_kho"]:
        print(f"-> Loi: Khong du hang trong kho! (Chi con {sp['ton_kho']})")
        return

    thanh_tien = so_luong_mua * sp["gia"]
    sp["ton_kho"] -= so_luong_mua

    lich_su_don_hang.append(
        {
            "ma_sp": ma_sp,
            "ten_sp": sp["ten_sp"],
            "so_luong": so_luong_mua,
            "thanh_tien": thanh_tien,
        }
    )

    print(
        f"-> Da ban {so_luong_mua} {sp['ten_sp']}. Tong tien: {thanh_tien:,} VND"
    )


def thong_ke_doanh_thu():
    print("\n--- THỐNG KÊ DOANH THU BÁN HÀNG ---")
    if not lich_su_don_hang:
        print("Chua co don hang nào duoc thuc hien.")
        return

    tong_doanh_thu = sum(dh["thanh_tien"] for dh in lich_su_don_hang)
    print("LICH SU BAN HANG:")
    for dh in lich_su_don_hang:
        print(
            f" - {dh['ma_sp']} | {dh['ten_sp']} | SL: {dh['so_luong']} | Thanh tien: {dh['thanh_tien']:,} VND"
        )
    print(f"\n>>> TONG DOANH THU: {tong_doanh_thu:,} VND")


def hien_thi_menu():
    print("\n===== QUẢN LÝ CỬA HÀNG MINI =====")
    print("1. Hien thi danh sach tat ca san pham")
    print("2. Xem cac san pham sap het hang")
    print("3. Them san pham moi")
    print("4. Ban hang / Tao don")
    print("5. Thong ke doanh thu")
    print("0. Thoat chuong trinh")


def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban (0-5): ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach_sp()
        elif lua_chon == "2":
            xem_sp_sap_het()
        elif lua_chon == "3":
            them_san_pham()
        elif lua_chon == "4":
            ban_hang()
        elif lua_chon == "5":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    chay_chuong_trinh()
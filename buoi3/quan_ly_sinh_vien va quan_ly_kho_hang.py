danh_sach_sv = [(8.5, "An"), (7.0, "Binh"), (9.2, "Chi"), (6.5, "Dung")]

danh_sach_sv.append((8.0, "Em"))

danh_sach_sv.remove((7.0, "Binh"))

danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

print("Chi co trong danh sach khong?", (9.2, "Chi") in danh_sach_sv)

danh_sach_sv.sort()
print("Danh sach sau khi sap xep theo diem tang dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")

danh_sach_sv.sort(reverse=True)
print("Danh sach sau khi sap xep theo diem giam dan:")
for diem, ten in danh_sach_sv:
    print(f"{ten} - {diem}")









    kho_hang = [
    ("Ban phim", 250000, 10),
    ("Chuot", 150000, 20),
    ("Man hinh", 2500000, 5),
]

# Them san pham moi
kho_hang.append(("Tai nghe", 300000, 15))

kho_hang.remove(("Chuot", 150000, 20))

print("DANH SACH KHO HANG:")
for ten, gia, so_luong in kho_hang:
    print(f"{ten:<12} - Gia: {gia:>10,} - SL: {so_luong}")

tong_gia_tri = 0
for ten, gia, so_luong in kho_hang:
    tong_gia_tri = tong_gia_tri + gia * so_luong

print(f"Tong gia tri kho hang: {tong_gia_tri:,} VND")
#hoat dong 5
tu_dien_anh_viet = {
    "hello": "xin chao", 
 "book": "quyen sach", 
 "table": "cai ban" 
} 

print(tu_dien_anh_viet.get("hello", "Khong tim thay tu nay")) 
print(tu_dien_anh_viet.get("computer", "Khong tim thay tu nay")) 

tu_dien_anh_viet["computer"] = "may tinh" 
 
tu_dien_anh_viet.pop("table") 
print("Tu dien hien tai:") 
for tu_anh, tu_viet in tu_dien_anh_viet.items(): 
 print(f"{tu_anh} - {tu_viet}")



 #hoat dong 6
doan_van = "python la ngon ngu lap trinh python de hoc python de dung" 
danh_sach_tu = doan_van.split() 
tan_suat = {} 
for tu in danh_sach_tu: 
 tan_suat[tu] = tan_suat.get(tu, 0) + 1 
print("Tan suat xuat hien cac tu:") 
for tu, so_lan in tan_suat.items(): 
 print(f"{tu}: {so_lan}")


 #hoat dong 7
 quan_ly_diem = { 
 "Nguyen Van A": [8.0, 7.5, 9.0], 
 "Tran Thi B": [6.0, 6.5, 5.5], 
 "Le Van C": [9.0, 9.5, 8.5],
} 
 
quan_ly_diem["Pham Thi D"] = [7.0, 8.0, 7.5] 

quan_ly_diem["Tran Thi B"][0] = 7.0 
diem_trung_binh = {} 
for ho_ten, danh_sach_diem in quan_ly_diem.items(): 
 diem_trung_binh[ho_ten] = round(sum(danh_sach_diem) / len(danh_sach_diem), 2) 
print("BANG DIEM TRUNG BINH:") 
for ho_ten, dtb in diem_trung_binh.items(): 
 dat_loai_gioi = dtb >= 8.0 
 print(f"{ho_ten:<15} - DTB: {dtb:<5} - Dat loai Gioi? {dat_loai_gioi}")


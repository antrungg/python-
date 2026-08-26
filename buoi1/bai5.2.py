diem = 6.5
tuoi = 20

# 1. Kiểm tra điểm đạt loại Khá (từ 6.5 đến dưới 8.0) dùng 'and'
is_kha = diem >= 6.5 and diem < 8.0
print("Điểm đạt loại Khá:", is_kha)

# 2. Kiểm tra tuổi chưa đủ 18 hoặc trên 60 dùng 'or'
is_dac_biet = tuoi < 18 or tuoi > 60
print("Tuổi chưa đủ 18 hoặc trên 60:", is_dac_biet)

# 3. Phủ định lại các điều kiện bằng 'not'
print("Phủ định điều kiện điểm Khá:", not (diem >= 6.5 and diem < 8.0))
print("Phủ định điều kiện tuổi:", not (tuoi < 18 or tuoi > 60))
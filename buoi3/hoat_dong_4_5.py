toa_do = (3, 5)
print(toa_do, type(toa_do))
toa_do[0] = 10



toa_do = (10, 20) 
x, y = toa_do
print("x =", x, "- y =", y)

a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)



c, d = 17, 5
thuong_du = divmod(c, d)
thuong, du = thuong_du

a, b = 10, 20
a, b = b, a
print("a =", a, "- b =", b)




import math

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
print(f"Khoang cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

cac_diem = [(0, 0), (3, 4), (6, 8)]

for x, y in cac_diem:

    khoang_cach_goc = math.sqrt(x ** 2 + y ** 2)
    print(f"Khoang cach tu diem {(x, y)} den goc toa do (0, 0) la: {round(khoang_cach_goc, 2)}")

    cac_diem = [(0, 0), (3, 4), (6, 8)]
for diem in cac_diem:
    x, y = diem
    kc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu điểm {diem} den goc toa do (0, 0) la: {round(kc, 2)}")
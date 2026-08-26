x = 10
print("Ban đầu x =", x)

x += 5
print("Sau khi x += 5  -> x =", x)

x -= 3
print("Sau khi x -= 3  -> x =", x)

x *= 2
print("Sau khi x *= 2  -> x =", x)

x /= 4
print("Sau khi x /= 4  -> x =", x)

x //= 2
print("Sau khi x //= 2 -> x =", x)

x **= 3
print("Sau khi x **= 3 -> x =", x)

print("-" * 30)

danh_sach = [1, 2, 3, "python"]

kiem_tra_in = 3 in danh_sach
print("3 có nằm trong danh_sach hay không?:", kiem_tra_in)

list1 = danh_sach
list2 = danh_sach
kiem_tra_is = list1 is list2
print("list1 và list2 cùng tham chiếu tới 1 list?:", kiem_tra_is)
import sqlite3

# Kết nối và tạo bảng
conn = sqlite3.connect("quan_ly_chi_tieu.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS chi_tieu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ten_khoan TEXT NOT NULL,
        so_tien REAL NOT NULL,
        danh_muc TEXT NOT NULL,
        ngay TEXT NOT NULL
    )
""")

# Chèn dữ liệu mẫu
du_lieu_mau = [
    ("Cơm trưa văn phòng", 55000, "Ăn uống", "10/11/2026"),
    ("Đổ xăng xe máy", 90000, "Đi lại", "10/11/2026"),
    ("Thanh toán tiền điện", 350000, "Hóa đơn", "11/11/2026"),
    ("Xem phim cuối tuần", 120000, "Giải trí", "11/11/2026")
]

cur.executemany("""
    INSERT INTO chi_tieu (ten_khoan, so_tien, danh_muc, ngay)
    VALUES (?, ?, ?, ?)
""", du_lieu_mau)

conn.commit()
conn.close()

print("Đã tạo thành công file 'quan_ly_chi_tieu.db' với dữ liệu mẫu!")
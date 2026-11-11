import datetime
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

import csdl_chitieu as db

DANH_SACH_DANH_MUC = ["Ăn uống", "Đi lại", "Mua sắm", "Giải trí", "Hóa đơn", "Khác"]

class UngDungQuanLyChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu ca nhan")
        # Tăng chiều cao cửa sổ lên 540 để không bị mất nút ở dưới
        self.geometry("560x540")
        self.resizable(False, False)
        
        # Khởi tạo CSDL
        db.tao_bang_neu_chua_co()
        
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_chi_tieu()

    def khoi_tao_giao_dien(self):
        # Frame 1: Thêm khoản chi mới
        khung_nhap = tk.LabelFrame(self, text="Thêm khoản chi mới", padx=10, pady=5)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Tên khoản chi:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ten.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Số tiền (VNĐ):").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_tien = tk.Entry(khung_nhap, width=30)
        self.o_nhap_tien.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh mục:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=27, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=2, column=1, padx=10, pady=5)

        btn_them = tk.Button(khung_nhap, text="Thêm chi tiêu", bg="#2e7d32", fg="white", 
                             font=("Arial", 9, "bold"), command=self.xu_ly_them_chi_tieu)
        btn_them.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame 2: Danh sách khoản chi tiêu (Chỉnh height=10 để nhường chỗ cho nút)
        khung_danh_sach = tk.LabelFrame(self, text="Danh sách các khoản chi tiêu", padx=5, pady=5)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=75, height=10)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chi_tieu.config(yscrollcommand=thanh_cuon.set)

        # Frame 3: Cụm 3 nút bấm thao tác ở dưới cùng
        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Thêm nhanh hôm nay", bg="#1976D2", fg="white", 
                  command=self.xu_ly_them_nhanh).grid(row=0, column=0, padx=5)

        tk.Button(khung_nut_thao_tac, text="Xóa khoản chi", bg="#D32F2F", fg="white", 
                  command=self.xu_ly_xoa_chi_tieu).grid(row=0, column=1, padx=5)

        tk.Button(khung_nut_thao_tac, text="Thống kê theo danh mục", bg="#E65100", fg="white", 
                  command=self.xu_ly_thong_ke).grid(row=0, column=2, padx=5)

    def tai_lai_danh_sach_chi_tieu(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for item in self.danh_sach_hien_tai:
            id_ct, ten, tien, danh_muc, ngay = item
            chuoi_hien_thi = f"[{ngay}] {ten} - {danh_muc} - ({tien:,.0f} VNĐ)"
            self.listbox_chi_tieu.insert(tk.END, chuoi_hien_thi)

    def xu_ly_them_chi_tieu(self):
        ten = self.o_nhap_ten.get().strip()
        tien_str = self.o_nhap_tien.get().strip()
        danh_muc = self.chon_danh_muc.get()
        ngay = datetime.date.today().strftime("%d/%m/%Y")

        if ten == "" or tien_str == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ tên khoản chi và số tiền.")
            return

        try:
            tien = float(tien_str)
        except ValueError:
            messagebox.showerror("Lỗi", "Số tiền nhập vào không hợp lệ.")
            return

        db.them_chi_tieu(ten, tien, danh_muc, ngay)
        
        self.o_nhap_ten.delete(0, tk.END)
        self.o_nhap_tien.delete(0, tk.END)
        self.tai_lai_danh_sach_chi_tieu()
        messagebox.showinfo("Thành công", f"Đã thêm khoản chi: {ten}")

    def xu_ly_them_nhanh(self):
        messagebox.showinfo("Thông báo", "Tự động lấy ngày hiện tại làm ngày ghi nhận!")

    def xu_ly_xoa_chi_tieu(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Lỗi", "Vui lòng chọn một khoản chi tiêu trong danh sách để xóa.")
            return

        id_chi_tieu = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_chi_tieu(id_chi_tieu)
        self.tai_lai_danh_sach_chi_tieu()

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_danh_muc()
        if not du_lieu:
            messagebox.showinfo("Thông báo", "Chưa có dữ liệu để thống kê.")
            return

        cac_danh_muc = [dong[0] for dong in du_lieu]
        so_tien = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_danh_muc, so_tien, color="cornflowerblue")
        plt.title("Số tiền chi tiêu theo danh mục")
        plt.xlabel("Danh mục")
        plt.ylabel("Số tiền (VNĐ)")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = UngDungQuanLyChiTieu()
    app.mainloop()
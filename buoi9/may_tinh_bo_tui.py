import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

bieu_thuc = tk.StringVar(value="")

entry_man_hinh = tk.Entry(cua_so, textvariable=bieu_thuc, font=("Arial", 18), justify="right", bd=10)
entry_man_hinh.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we")

def nhan_nut(gia_tri):
    bieu_thuc.set(bieu_thuc.get() + str(gia_tri))

def xoa_man_hinh():
    bieu_thuc.set("")

def tinh_ket_qua():
    try:
        ket_qua = eval(bieu_thuc.get())
        bieu_thuc.set(str(ket_qua))
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")
        bieu_thuc.set("")

danh_sach_nut = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in danh_sach_nut:
    if text == '=':
        cmd = tinh_ket_qua
    elif text == 'C':
        cmd = xoa_man_hinh
    else:
        cmd = lambda t=text: nhan_nut(t)
        
    tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, command=cmd)\
      .grid(row=row, column=col, padx=5, pady=5)

if __name__ == "__main__":
    cua_so.mainloop()
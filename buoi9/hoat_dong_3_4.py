#hoat dong 3
#bai 3.1
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Vi du Listbox") 
cua_so.geometry("300x250") 
listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single") 
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]: 
 listbox_mon_hoc.insert(tk.END, mon) 
listbox_mon_hoc.pack(pady=10) 
def xem_mon_da_chon(): 
    lua_chon = listbox_mon_hoc.curselection()

    if lua_chon: 
          nhan_ket_qua.config(text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}") 
tk.Button(cua_so, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=5) 
nhan_ket_qua = tk.Label(cua_so, text="") 
nhan_ket_qua.pack() 
cua_so.mainloop()


#bai3.2
import tkinter as tk
from tkinter import ttk
cua_so = tk.Tk()
cua_so.title("Vi du Combobox")
cua_so.geometry("300x180")
tk.Label(cua_so, text="Chon thanh pho:").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM",
"Hue"])
combobox_thanh_pho.current(0) 
combobox_thanh_pho.pack(pady=5)
def xem_thanh_pho():
 nhan_ket_qua.config(text=f"Ban chon: {combobox_thanh_pho.get()}")
tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()
cua_so.mainloop()


#Hoat dong 4
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Vi du Scale") 
cua_so.geometry("300x180") 
def khi_keo_thanh_truot(gia_tri): 
 nhan_gia_tri.config(text=f"Gia tri hien tai: {gia_tri}") 
thanh_truot = tk.Scale(cua_so, from_=0, to=100, orient="horizontal",  command=khi_keo_thanh_truot) 
thanh_truot.pack(pady=20, padx=20, fill="x")
nhan_gia_tri = tk.Label(cua_so, text="Gia tri hien tai: 0") 
nhan_gia_tri.pack() 
cua_so.mainloop()


#hoat dong 5
import tkinter as tk 
cua_so = tk.Tk() 
cua_so.title("Vi du bien dieu khien") 
cua_so.geometry("350x220") 
bien_ho_ten = tk.StringVar(value="Nguyen Van A") 
bien_tuoi = tk.IntVar(value=18) 
bien_dong_y_dieu_khoan = tk.BooleanVar(value=False) 
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w") 
tk.Entry(cua_so, textvariable=bien_ho_ten).grid(row=0, column=1, padx=10, pady=10) 
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w") 
tk.Entry(cua_so, textvariable=bien_tuoi).grid(row=1, column=1, padx=10, pady=10) 
tk.Checkbutton(cua_so, text="Dong y dieu khoan", variable=bien_dong_y_dieu_khoan).grid(  row=2, column=0, columnspan=2, pady=10) 
def xem_gia_tri_bien(): 
 print("Ho ten (StringVar):", bien_ho_ten.get()) 
 print("Tuoi (IntVar):", bien_tuoi.get()) 
 print("Dong y dieu khoan (BooleanVar):", bien_dong_y_dieu_khoan.get())  
 bien_tuoi.set(bien_tuoi.get() + 1)  
tk.Button(cua_so, text="Xem gia tri bien (va +1 tuoi)", command=xem_gia_tri_bien).grid(  row=3, column=0, columnspan=2, pady=10) 
cua_so.mainloop()


#hoat dong 6
import tkinter as tk
from tkinter import messagebox 
def xu_ly_submit(): 
 ho_ten = entry_ho_ten.get().strip() 
 tuoi_nhap = entry_tuoi.get().strip() 
 email = entry_email.get().strip() 
 if ho_ten == "": 
  messagebox.showerror("Loi", "Ho ten khong duoc de trong.") 
  return 
 try: 
   tuoi = int(tuoi_nhap) 
 except ValueError: 
  messagebox.showerror("Loi", "Tuoi phai la mot so nguyen.") 
 return 
 if "@" not in email: 
  messagebox.showerror("Loi", "Email khong hop le (thieu ky tu @).")  
  return 
  messagebox.showinfo("Thanh cong", f"Da nhan thong tin: {ho_ten} - {tuoi} tuoi - {email}") 
cua_so = tk.Tk() 
cua_so.title("Form co validate") 
cua_so.geometry("380x220") 
tk.Label(cua_so, text="Ho ten:").grid(row=0, column=0, padx=10, pady=10, sticky="w") 
entry_ho_ten = tk.Entry(cua_so, width=25) 
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10) 
tk.Label(cua_so, text="Tuoi:").grid(row=1, column=0, padx=10, pady=10, sticky="w") 
entry_tuoi = tk.Entry(cua_so, width=25) 
entry_tuoi.grid(row=1, column=1, padx=10, pady=10) 
tk.Label(cua_so, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="w") 
entry_email = tk.Entry(cua_so, width=25) 
entry_email.grid(row=2, column=1, padx=10, pady=10) 
tk.Button(cua_so, text="Submit", command=xu_ly_submit).grid(row=3, column=0,  columnspan=2, pady=15) 
cua_so.mainloop()

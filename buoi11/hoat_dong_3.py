import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("buoi11/hoatdong2/diem_sinh_vien.csv")


diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

plt.figure(figsize=(6, 4))
bars = plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f"{yval:.2f}", ha='center', va='bottom', fontweight='bold')

plt.ylim(0, 10)
plt.title("DIEM TRUNG BINH THEO MON HOC", fontweight='bold')
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.grid(axis='y', linestyle='--', alpha=0.5)


plt.savefig("bieu_do_cot.png")
plt.show()



lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green", label="Diem thuc te")


for i, txt in enumerate(diem_qua_cac_lan):
    plt.annotate(f"{txt}", (lan_kiem_tra[i], diem_qua_cac_lan[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color='green')

plt.xticks(lan_kiem_tra, ["Lan 1", "Lan 2", "Lan 3"])
plt.ylim(0, 10)
plt.title("XU HUONG DIEM QUA CAC LAN KIEM TRA", fontweight='bold')
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem so")
plt.legend(loc="upper left")
plt.grid(linestyle='--', alpha=0.5)


plt.savefig("bieu_do_duong.png")
plt.show()
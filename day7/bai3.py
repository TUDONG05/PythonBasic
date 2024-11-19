ma_hoc_phan = ["IT6002", "IT6126", "IT6067", "IT6120"]
chi_tiet = [
    {"ten_mon_hoc": "Cau truc du lieu va giai thuat", "so_tin_chi": 3},
    {"ten_mon_hoc": "He thong co so du lieu", "so_tin_chi": 4},
    {"ten_mon_hoc": "Kien truc may tinh va he dieu hanh", "so_tin_chi": 3},
    {"ten_mon_hoc": "Lap trinh huong doi tuong", "so_tin_chi": 3}
]

du_lieu = {ma_hoc_phan[i]: chi_tiet[i] for i in range(len(ma_hoc_phan))}
# print(du_lieu)

def loc_mon_hoc(du_lieu):
    return {
        ma_hoc_phan: chi_tiet
        for ma_hoc_phan, chi_tiet in du_lieu.items()
        if (len(chi_tiet["ten_mon_hoc"].split()) > 5) and ( chi_tiet["so_tin_chi"] >= 3)
    }

kq = loc_mon_hoc(du_lieu)
print("ket qua:", kq)

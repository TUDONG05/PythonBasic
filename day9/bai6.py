def dem_tu_trong_chuoi(chuoi):
    tach = chuoi.split()
    # tach chuoi thanh danh sach cac tu de dem
    return len(tach)
    # dung len() de dem do dai list gom cac tu vua tach

chuoi = input("nhap chuoi:")
print(dem_tu_trong_chuoi(chuoi))
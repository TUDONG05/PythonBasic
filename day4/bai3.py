
tuple1 = ('HAT','Min','Justatie','Bray','Kimises')
tuple2= ('DSK','Thái VG','MCK','Bray','Pháo','Kimises')

print("cac phan tu thuoc tuple 1 nhung ko thuoc tuple 2:")
for i in tuple1:
    if i not in tuple2:
        print(i,)

print("cac phan tu thuoc tuple 2 nhung khong thuoc tuple 1:")
for j in tuple2:
    if j not in tuple1:
        print(j,)

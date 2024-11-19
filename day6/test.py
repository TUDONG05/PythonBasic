
# kiem tta day con co xuat hienj trong chuoi bo khong

def ktra(chuoi_bo, chuoi_con):
    if chuoi_con in chuoi_bo:
        return True
    else:
        return False

chuoi_bo ="Hello, world!"
chuoi_con1 ="world"
chuoi_con2 ="Python"
print(ktra(chuoi_bo,chuoi_con1))
print(ktra(chuoi_bo,chuoi_con2))


# viet chuong trinh tinh tong hieu tich thuong cua 2 so nguyen va in ra man hinh

a = int(input("a="))
b = int(input("b="))
print("tong cua",a,"va",b,"la", (a +b))
print("hieu cua",a,"va",b,"la", (a -b))
print("tich cua",a,"va",b,"la", (a *b))

if b==0:
    print("ko the chia cho so 0")
else:
    print("thuong cua",a,"va",b,"la", (a /b))

# tao list co 5 so nguyen
# 1. in ra man hinh
# 2.them 1 so nguyen moi 
# 3. loai bo 1 so khoi list theo value hoac index 
# 4. sap tang dan va in ra man hinh


list=[]
n = int(input("nhap so phan tu muon nhap vao list: "))
for i in range(n):
    a = int(input("nhap so nguyen: "))
    list.append(a)


print("list vua nhap la: ", list)

x =int(input("Nhap so muon xoa khoi list:"))
# TH1: xoa so dau tien
if x in list:
    list.remove(x)
else:
    print("ko co phan tu",x,"trong list")
print("list sau khi xoa so",x,"dau tien:",list)

# TH2: xoa nhieu so
if x not in list:
    print("khon ton tai phan tu",x,"trong list")
else:
    for i in list:
        if i is x:
            list.remove(i)
    print("list sau khi xoa tat ca so",x,"la: ",list)

# them 1 so vao list
b = int(input("nhap so muon them: "))
list.append(b)
print("list sau khi them:",list)

# sap xep list tang dan 
list.sort()
print("list sau khi xep tang dan:",list)





# set

input1 =input("nhap cac phan tu cua set1:")
set1 =set(input1.split(','))
print(set1)

input2 =input("nhap cac phan tu cua set 2:")
set2 =set(input2.split(','))
print(set2)

hop=set1.union(set2)
print("hop 2 set: ",hop)

giao=set1.intersection(set2)
print("giao 2 set la: ",giao)



# dictionanry

# nhap thong tin
ten=input("nhap ten:")
tuoi=int(input("nhap tuoi:"))
dia_chi=input("nhap dia chi:")

# tao 1 dict
nguoi ={
    "ten":ten,
    "tuoi":tuoi,
    "dia_chi":dia_chi
}

# in thong tin
print("thong tin cua nguoi:")
print("Ten:",nguoi["ten"])
print("tuoi:",nguoi["tuoi"])
print("Dia chi:",nguoi["dia_chi"])



# nhap 1 list,chuyen list ve tuple, in ra man hinh

nhap=input("nhap cac phan tu cac nhau boi dau ',' :")
list=nhap.split(',')
# chuyen list ve tuple
a = tuple(list)
print("list vua nhap la: ", list)
print("tuple thu duoc la: ",a)

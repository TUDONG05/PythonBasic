N = int(input("Nhap so phan tu: "))
ml=[]
for i in range(1,N+1):
    a= int(input("nhap so nguyen:"))
    ml.append(a)
print(ml)

# 1.dem so lan xuat hien cua x trong list

x = int(input("nhap so x: "))
# cach 1 dung phuong thuc count()
print("trong list co so phan tu x la: ",ml.count(x))


# cach 2 dung vong for duyet tung gia tri trong list
count =0
for i in ml:
    if i==x:
        count+=1
print("so lan xuat hien cua ",x,"trong list la ",count)


# 2. them phan tu vao dau list : <ten_list>[:0]=[gia_tri_can_chen]
b = int(input("Nhap so muon chen vao dau list:"))
ml[:0] = [b]
print(ml)

#  them phan tu vao cuoi list.

# cach 1: chen vao len- vi tri cuoi cung <ten_list>[len(ten_list):]=[gia_ tri _can_ chen]
c = int(input("nhap so muon chen vao cuoi list:"))
ml[len(ml):]=[c]
print(ml)

# cach 2: dung cau lenh <ten_list>.append(gia_tri_can_ chen)
ml.append(5)
print(ml)





# 3.xay dung day fibonancci
ml = []

N = int(input("Nhap so phan tu: "))
a= 0
b= 1
for i in range(N):
    ml.append(a)
    a,b=b,a+b
print(ml)
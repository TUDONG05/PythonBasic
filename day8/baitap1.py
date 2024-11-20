n = int(input("n="))
while n >5:
   n = int(input("n=")) 


list =[]
for i in range(n):
    MSV =input("MaSV:")
    hoTen =input("Ho ten: ")
    gioiTinh = input("Gioi tinh: ")
    diem = float(input("Diem: "))
    list.append([MSV,hoTen,gioiTinh,diem])

# sep mang tang dan
list.sort(key = lambda x:x[3])  
# print("Top 3 co diem cao nhat: ", list[])
for i in range(3):
    print(list[i])

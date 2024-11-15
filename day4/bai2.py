# bai 2
n = int (input("nhap vao so N:"))
ml =[]



for i in range(n):
    a1 = input("nhap MSV va ten:")
    a2 = int(input("nhap so buoi: "))
    ml.append([a1,a2])
print(ml)

print("Danh sach di it nhat:")


# tim so buoi it nhat
m = ml[0][1]
for i in range(n):
    if(ml[i][1]<= m):
        m = ml[i][1]
for i in range(n):
    if(ml[i][1]==m):
        print(ml[i])




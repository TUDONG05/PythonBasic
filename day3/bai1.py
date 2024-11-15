# day 3
# rang(start,stop,step)--tra ve chuoi so tang dan
# bai1
# a)
# n = int(input("nhap vao so nguyen duong: "))
# t =0
# for i in range(1,n):
#     t+=i
# print(t)

# b)
# t=0
# for i in range(1,n):
#     if i % 3!=0 :
#         print(i)
#         if (i %10==0):
#             break

# c)
# import math
# def snt(n):
#     if n<=1:
#         return False
#     for i in range(2, int(math.sqrt(n)+1)):
#         if n % i==0:
#             return False
#     return True
    
            
# def tong(n):
#     t=0
#     for i in range(2,n +1):
#         if not snt(i):
#          continue
#         t +=i
#     return t
# print("tong cac snt tu 1 --> n: ", tong(n))



n =int(input("n="))

 
print("Ve tam giac sao deu:");
for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end = " ");
    for k in range(1, i+1):
        print("*", end=" ");
    print()

# vong for 1 dieu khien cac hang
# vong for 2 in ra ki tu trong
# vong for 3 in ra ki tu *
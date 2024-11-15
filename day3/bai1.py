# day 3
# rang(start,stop,step)--tra ve chuoi so tang dan
#enumerate


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
# n = int(input("n="))
# tong =0
# for i in range(2,n):
#     check =True
#     for j in range(2,int(math.sqrt(i))+1):
#         if(i%j==0):
#             check = False
#             break
        
#     if check:
#         print(i)
#         tong+=i
# print(tong)




# d)
# n =int(input("n="))
# print("Ve tam giac sao deu:")
# for i in range(1, n+1):
#     for j in range(1, n+1-i):
#         print("", end = " ")
#     for k in range(1, i+1):
#         print("*", end=" ")
#     print()

# vong for 1 dieu khien cac hang
# vong for 2 in ra ki tu trong
# vong for 3 in ra ki tu *
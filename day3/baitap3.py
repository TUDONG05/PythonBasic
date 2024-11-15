
for n in range(1,1000):
# tinh tong uoc duong
    tong =0
    for i in range(1,n):
        if n % i ==0:
            tong+=i
    if n == tong:
        print(n," la so hoan hao")
    else:
        print(n, "khong hoan hao")


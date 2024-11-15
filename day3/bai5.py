buoc =0
n = int(input("n="))
while n!=1:
    if n%2==0:
        n/=2
        buoc+=1
    else:
        n=n*3+1
        buoc+=1
print(buoc)
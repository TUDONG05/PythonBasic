def tim_cac_so_chan(n):
    chan =[]
    for i in range(1,n+1):
        if i % 2 == 0:
            chan.append(i)
    return chan
            

n =int(input("n="))
print(tim_cac_so_chan(n))

khm =input("Khach hang moi: ")
sl =int(input("nhap so luong san pham: "))
tgt= float(input("nhap tong gia tri don hang: "))


if khm == "yes":
    stGiam=0.15 * tgt
elif khm =="no": 
    stGiam=0.1 * tgt


if (sl >=6 ) and (sl<=10):
    stGiam +=0.05*tgt
elif(sl >10):
    stGiam +=0.1*tgt

if 10000 < tgt < 50000:
    stGiam+=tgt*0.5
else:
    stGiam+=tgt*0.15


if(khm =="yes") and (sl > 10) and (tgt>100000):
    stGiam+=0.2*tgt

print("tong gia tri cuoi cung sau khi giam gia la:", tgt - stGiam)


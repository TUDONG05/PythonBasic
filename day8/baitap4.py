s1 = input("nhap chuoi 1:")
s2 =input("nhap chuoi 2:")

if len(s1)>len(s2):
    s1 =s1[len(s1)-len(s2):]
elif len(s1)<len(s2):
    s2 =s2[len(s2) - len(s1):]
print(s1+s2)
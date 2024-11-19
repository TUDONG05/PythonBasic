# s = input("nhap chuoi: ")
# print("apple",s.count("apple"))
# print("banana",s.count("banana"))
# print("kiwi",s.count("kiwi"))
# print("mango",s.count("mango"))
# print("grape",s.count("grape"))

dz = int(0)
dzz =int(0)
dzzz =int(0)
dzzzz =int(0)
s = input("nhap chuoi:")
a = s.split()
print(a)

for i in a:
    if(i=='z'):
        dz+=1

for i in a:
    if(i=='zz'):
        dzz+=1

for i in a:
    if(i=='zzz'):
        dzzz+=1

for i in a:
    if(i=='zzzz'):
        dzzzz+=1
print("z",dz)
print("zz",dzz)
print("zzz",dzzz)
print("zzzz",dzzzz)

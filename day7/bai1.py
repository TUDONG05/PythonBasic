set1=set({})
set2=set({})
n =int(input("Nhap so phan tu set1:"))
for i in range(n):
    a = int(input("nhap phan tu:"))
    set1.add(a)


m = int(input("Nhap so phan tu set 2:"))
for i in range(m):
    b = int(input("nhap phan tu: "))
    set2.add(b)

print(set1)
print(set2)
# 1. tao ra 1 set moi gom tat ca cac phan tu cua 2 set va in ra
set_hop=set1 | set2
print("hop cua 2 set: ",set_hop)
# 2. tao ra 1 set moi gom cac phan tu giong nhau cua 2 set va in ra man hinh
set_giao=set1.intersection(set2)
print("giao cua 2 set: ",set_giao)
# 3. In ra màn hình những phần tử có trong set 1 mà không có trong set 2, và ngược lại
print("phần tử có trong set 1 mà không có trong set 2: ", set1-set2)
print("phần tử có trong set 2 mà không có trong set 1: ", set2-set1)
# 4. Kiểm tra xem set 1 có phải là tập con hay tập chứa của set 2 hay không?
check_sub = set1.issubset(set2)
if check_sub:
    print("set 1 la tap con cua set 2")
else:
    print("set 1 ko la tap con cua set 2")

check_super =set1.issuperset(set2)
if check_super:
    print("set1 la tap chua cua set2")
else:
    print("set1 ko la tap chua cua set2")
# 5. In ra dãy đã sắp xếp ở câu 1
print(sorted(set_hop))
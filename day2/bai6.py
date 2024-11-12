
a =float(input("nhap chieu cao cua An: "))
l =float(input("nhap chieu cao cua Linh:"))
d =float(input("nhap chieu cao cua Duc:"))
n =float(input("nhap chieu cao cua Nam: "))

print ( ((a > l and a > d and a > n) and (" An cao nhat" )) 
       or ((l > a and l > d and l > n) and ("Linh cao nhat ")  )
       or ((d > a and d> l and d>n) and ("duc cao nhat"))
       or (  (n > a and n > d and n > l) and ("nam cao nhat "))) 

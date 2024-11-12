import math
x1 = float(input("x1= "))
y1 = float(input("y1= "))
kcA = math.sqrt(x1 * x1 + y1 * y1)
x2 = float(input("x2="))
y2 = float(input("y2="))
kcB = math.sqrt(x2*x2 + y2*y2)
x3=float(input("x3="))
y3 = float(input("y3="))
kcC =math.sqrt(x3 * x3 + y3*y3)


if (kcA > kcB ) and (kcA > kcC):
    print("Nha A xa truong nhat")
elif(kcB > kcC):
    print("nha B xa truong nhat")
else: 
    print("nha C xa truong nhat")
if (kcA < kcB ) and (kcA < kcC):
    print("Nha A gan truong nhat")
elif(kcB < kcC):
    print("nha B gan truong nhat")
else: 
    print("nha C gan truong nhat")


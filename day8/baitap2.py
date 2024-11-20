
list=[]
n = int(input("n="))
for i in range(n):
    s =input("nhap chuoi:")
    list.append(s)

def checkAZ(string):
    letter=False
    number=False

    for i in string:
        if 'a' <= i <= 'z':
            letter=True
        elif '0' <= i <= '9':
            number =True
        else:
            return False
    return len(string) >=6 and letter and number


dem=0
for i in list:
    if checkAZ(i):
        dem+=1
print(dem)
mang1=('tài', 'thùy','thạch', 'trường', 'tiến')
mang2=('hải', 'tài', 'nhật minh', 'cao minh', 'đặng anh', 'hùng', 'trường')
# cac pt thuoc mang 1 nhung ko thuoc mang 2
for i in mang1:
    if i not in mang2:
        print(i,)
# cac pt thuoc mang 2 nhung ko thuoc mang 1
for i in mang2:
    if i not in mang1:
        print(i,)
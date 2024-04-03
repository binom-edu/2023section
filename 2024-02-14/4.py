d = int(input())
a = int(input())

h = a * 2
if h % d == 0:
    print(a)
else:
    print((h + (d - h % d)) // 2)
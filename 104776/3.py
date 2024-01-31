n = int(input())
k = int(input())
if k <= n - 1:
    print(4)
elif k == 2 * n:
    print(6)
elif k == n:
    print(3)
else:
    print(5)
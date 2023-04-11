def f(x):
    ans = 0
    while x:
        ans += x % 10
        x //= 10
    return ans

a, b = map(int, input().split())
for i in range(a, b + 1):
    for m in range(2, 10):
        if f(i) != f(i * m):
            break
    else:
        print(i, end=' ')
print()
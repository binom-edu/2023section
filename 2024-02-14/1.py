x, y = map(int, input().split())

ans = 1
for i in range(x + y):
    if i == 0:
        ans = 2
    else:
        ans += 4 * i
print(ans + x)


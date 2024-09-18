n, k = map(int, input().split())
ans = 1
for i in range(n):
    if i < k:
        ans *= 3
    elif i < 2 * k:
        ans *= 2

print(ans)
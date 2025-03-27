a, b = map(int, input().split())
ans = 0
for x in range(a, b + 1):
    if x == 1:
        continue
    d = 2
    while d ** 2 <= x:
        if x % d == 0:
            break
        d += 1
    else:
        ans += 1
print(ans)
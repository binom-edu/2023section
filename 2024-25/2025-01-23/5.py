d, l, r = map(int, input().split())

ans = 0
p = 1
while p ** 2 < d:
    if d % p == 0:
        q = d // p
        if (p + q) % 2 == 0:
            x = (p + q) // 2
            y = q - x
            if y > 0 and l <= y**2 < x**2 <= r:
                ans += 1
    p += 1
print(ans)

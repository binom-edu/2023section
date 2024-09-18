def d(x, y):
    return (x ** 2 + y ** 2) ** 0.5

a = [(0, 0), (2, 3), (5, 7)]

ans = 0
for x, y in a:
    ans = max(ans, d(x, y))

print(ans)
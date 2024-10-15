def f(n):
    return n * (n + 1) // 2 <= r - l

out = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    le = 0
    ri = r
    while ri - le > 1:
        m = (le + ri) // 2
        if f(m):
            le = m
        else:
            ri = m
    out.append(le + 1)

for i in out:
    print(i)
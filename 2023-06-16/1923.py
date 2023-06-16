def f(d):
    return (d // w) * (d // h)

w, h, n = map(int, input().split())

l = 0
r = w * n

while r - l > 1:
    m = (r + l) // 2
    if f(m) < n:
        l = m
    else:
        r = m

print(r)
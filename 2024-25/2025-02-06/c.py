def f(x):
    return  (x <= a or x >= b) and \
            (x > c and x < d) and \
            (x % 2 != 0 or x <= e)

for _ in range(int(input())):
    a, b, c, d, e = map(int, input().split())
    x = c + 1
    if f(x):
        print(x)
        continue
    if x > a and b > c:
        x = b
        if f(x):
            print(x)
            continue
    if x % 2 == 0:
        x += 1
    if f(x):
        print(x)
    else:
        print(-1)
    
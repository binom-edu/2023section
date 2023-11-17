cnt = 0
for i in range(8800, 55535 + 1):
    prod = 1
    n = i
    has7 = False
    while n:
        d = n % 10
        if d == 7:
            has7 = True
        prod *= d
        n //= 10
    if prod > 35 and has7:
        cnt += 1
        maxx = i
print(maxx, cnt)
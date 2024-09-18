n = int(input())
x = 0
while n:
    d = n % 10
    if (x >> d) & 1:
        print('YES')
        exit(0)
    x |= (1 << d)
    n //= 10
print('NO')
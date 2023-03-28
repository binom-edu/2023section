a, b = map(int, input().split())
for n in range(a, b + 1):
    n1 = n
    while n1 > 0:
        d = n1 % 10
        n1 //= 10
        if d == 0 or n % d != 0:
            break
    else:
        print(n, end=' ')
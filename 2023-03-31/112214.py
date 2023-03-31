n = int(input())
prev = -1
while n:
    d = n % 10
    if d == prev:
        print('yes')
        break
    prev = d
    n //= 10
else:
    print('no')
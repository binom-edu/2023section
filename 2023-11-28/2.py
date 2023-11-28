def r(n):
    s = bin(n)[2:]
    for i in range(2):
        s += str(s.count('1') % 2)
    return int(s, 2)

n = 1
while r(n) <= 77:
    n += 1
print(n, r(n))
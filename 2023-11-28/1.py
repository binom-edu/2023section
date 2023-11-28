n = 78
while bin(n).count('1') % 2 != 0:
    n += 1

print(n // 4)
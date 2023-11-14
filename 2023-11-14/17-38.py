with open('17-38.txt') as fin:
    a = [int(i) for i in fin]

n = len(a)
min6 = min([i for i in a if abs(i) % 10 == 6])

cnt = 0
max_s = -10 ** 9
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    if ((abs(x) % 10 == 6) ^ (abs(y) % 10 == 6)) and x ** 2 + y ** 2 < min6 ** 2:
        cnt += 1
        max_s = max(max_s, x ** 2 + y ** 2)

print(cnt, max_s)
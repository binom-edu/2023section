with open('17-1.txt') as fin:
    a = [int(i) for i in fin]

n = len(a)
cnt = 0
min_s = 10 ** 9
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    if x % 9 == 0 and y % 9 == 0:
        cnt += 1
        min_s = min(min_s, x + y)
print(cnt, min_s)
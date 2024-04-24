import sys
sys.stdin = open('26-3.txt')
n, s = map(int, input().split())
a = []
for i in range(n):
    t = input().split()
    t[1] = int(t[1])
    t[2] = int(t[2])
    a.append(t)

a.sort(key=lambda x: [x[0], -x[1]], reverse=True)

cnt_a = 0
for i in a:
    typ, price, amount = i
    cnt = min(amount, s // price)
    if i[0] == 'A':
        cnt_a += cnt
    s -= cnt * price

print(cnt_a, s)
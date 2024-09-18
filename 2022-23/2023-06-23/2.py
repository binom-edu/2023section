# заполнение нулями

n, m = map(int, input().split())

a = [[0 for i in range(m)] for j in range(n)]

for i in a:
    print(*i)

print('----')

a[1][2] = 7
for i in a:
    print(*i)
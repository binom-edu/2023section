n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])

b = [[0 for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        b[i][j] = a[j][i]

maxx = max([max(i) for i in a])

for i in b:
    if maxx in i:
        print(*i)
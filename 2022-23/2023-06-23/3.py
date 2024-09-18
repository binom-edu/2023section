# заполнение по порядку

n, m = map(int, input().split())

a = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        x = i * m + j
        a[i][j] = x
        
for i in a:
    print(*i)
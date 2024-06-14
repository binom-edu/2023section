import sys
sys.stdin = open('g.txt', 'r')
sys.stdout = open('g.out', 'w')

n, m = map(int, input().split())
g = []
for i in range(n):
    g.append(dict())
for i in range(m):
    u, v, x = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = x
    g[v][u] = x
print(g)

INF = 10 ** 6
c = [0] * n
d = [INF] * n

start = 0
d[start] = 0
cur = start
min_d = 0

while min_d != INF:
    c[cur] = 1
    for u in g[cur]:
        d[u] = min(d[u], d[cur] + g[cur][u])
    min_d = INF
    for v in range(n):
        if c[v] == 0 and d[v] < min_d:
            min_d = d[v]
            cur = v
print(d)
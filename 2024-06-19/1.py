import sys
sys.stdin = open('dijkstra.in')
sys.stdout = open('dijkstra.out', 'w')

n, s, f = map(int, input().split())
s -= 1
f -= 1

g = []
for i in range(n):
    g.append([int(j) for j in input().split()])

INF = 10 ** 6
c = [0] * n
d = [INF] * n

start = s
d[start] = 0
cur = start
min_d = 0
prev = [-1] * n

while min_d != INF:
    c[cur] = 1
    for u in range(n):
        if u != cur and g[cur][u] != -1:
            if d[cur] + g[cur][u] < d[u]:
                d[u] = d[cur] + g[cur][u]
                prev[u] = cur
            d[u] = min(d[u], d[cur] + g[cur][u])
    min_d = INF
    for v in range(n):
        if c[v] == 0 and d[v] < min_d:
            min_d = d[v]
            cur = v
if d[f] == INF:
    print(-1)
else:
    print(d[f])
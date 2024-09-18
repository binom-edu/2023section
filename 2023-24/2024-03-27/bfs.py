import sys
sys.stdin = open('g.txt')

n, m = map(int, input().split())
g = []
for i in range(n):
    g.append([])

for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dist = [-1] * n
start = 0
q = [start]
dist[start] = 0
while q:
    v = q.pop(0)
    for u in g[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            q.append(u)
print(*dist)
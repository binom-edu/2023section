import sys
sys.stdin = open('g.txt')

n, m = map(int, input().split())
g = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1
for i in g:
    print(*i)

# Проверить, что u - сосед v
print(g[0][4])
print(g[2][4])

# Найти всех соседей вершины 2
for i in range(n):
    if g[2][i] == 1:
        print(i, end=' ')
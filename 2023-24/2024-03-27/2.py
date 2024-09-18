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

print(g)

# Проверить, что u - сосед v
print(4 in g[0])
print(4 in g[2])

# Найти всех соседей вершины 2
print(*g[2])
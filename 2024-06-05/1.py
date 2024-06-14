import sys
sys.setrecursionlimit(1000)

sys.stdin = open('g.txt')

def dfs(v):
    print('->', v)
    used[v] = True
    for u in g[v]:
        if not used[u]:
            dfs(u)
    print('<-', v)


n, m = map(int, input().split())
g = []
for i in range(n):
    g.append([])

for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

used = [False] * n

dfs(0)
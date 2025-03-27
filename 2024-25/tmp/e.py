from collections import deque
import sys
input = sys.stdin.readline

out = []
def bfs(gr, v, c):
    col[v] = c
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for u in gr[v]:
            if col[u] == 0:
                col[u] = c
                q.append(u)
    

for _ in range(int(input())):
    n, m1, m2 = map(int, input().split())
    g = []
    for i in range(n): g.append(set())
    f = []
    for i in range(n): f.append(set())
    e = []
    for i in range(m1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        e.append([a, b])
        f[a].add(b)
        f[b].add(a)
    for i in range(m2):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].add(b)
        g[b].add(a)
    col = [0] * n
    c = 0
    for v in range(n):
        if col[v] == 0:
            c += 1
            bfs(g, v, c)
    cg = c
    del g
    ans = 0
    for u, v in e:
        if col[u] != col[v]:
            f[u].remove(v)
            f[v].remove(u)
            ans += 1
    del e
    col = [0] * n
    c = 0
    for v in range(n):
        if col[v] == 0:
            c += 1
            bfs(f, v, c)
    out.append(ans + c - cg)

for i in out:
    print(i)
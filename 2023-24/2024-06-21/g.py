import sys
sys.stdin = open('distance.in')
sys.stdout = open('distance.out', 'w')

n, m = map(int, input().split())
s, f = map(int, input().split())
s -= 1
f -= 1

g = []
for i in range(n):
    g.append({})

for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = w
    g[v][u] = w

INF = 10 ** 12
c = [False] * n
d = [INF] * n
prev = [-1] * n

cur = s
d[cur] = 0
min_d = 0

while min_d != INF:
    c[cur] = True
    for u in g[cur]:
        if d[cur] + g[cur][u] < d[u]:
            d[u] = d[cur] + g[cur][u]
            prev[u] = cur

    min_d = INF
    for v in range(n):
        if not c[v] and d[v] < min_d:
            min_d = d[v]
            cur = v
cur = f
st = [f + 1]
while cur != s:
    st.append(prev[cur] + 1)
    cur = prev[cur]

st.reverse()
print(d[f])
print(*st)
import sys
import copy
sys.stdin = open('g.txt')

n, m = map(int, input().split())
INF = 10 ** 9
g = [[INF for i in range(n)] for j in range(n)]


for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    g[u][v] = w
    g[v][u] = w

dp = copy.deepcopy(g)

for k in range(n):
    for i in range(n):
        for j in range(n):
            # if g[i][k] == INF or g[k][j] == INF:
            #     continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            # dp[i][j] - длина мин. пути от вершины i до вершины j

# if dp[i][j] > INF // 100:
    # считаем бесконечностью
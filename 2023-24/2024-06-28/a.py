import sys
sys.stdin = open('floyd.in')
sys.stdout = open('floyd.out', 'w')

n = int(input())
g = []
for i in range(n):
    g.append([int(j) for j in input().split()])

for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][j], g[i][k] + g[k][j])

for i in g:
    print(*i)
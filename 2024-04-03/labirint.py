import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
g = []
for i in range(n * m):
    g.append([])
for i in range(n):
    s = input()
    for j in range(m):
        v = i * m + j
        code = s[j]
        i_code = int(code, 16)
        b_code = bin(i_code)[2:].rjust(4, '0')
        u, r, d, l = b_code
        if u == '1':
            g[v].append(v - m)
        if r == '1':
            g[v].append(v + 1)
        if d == '1':
            g[v].append(v + m)
        if l == '1':
            g[v].append(v - 1)

x, y = map(int, input().split())
x -= 1
y -= 1
start = x * m + y
x, y = map(int, input().split())
x -= 1
y -= 1
end = x * m + y

q = []
d = [-1] * m * n
d[start] = 0
q.append(start)

pre = [-1] * m * n
while q:
    v = q.pop(0)
    for u in g[v]:
        if d[u] == -1:
            d[u] = d[v] + 1
            q.append(u)
            pre[u] = v
print(d[end])

v = end
ans = [end]
while pre[v] != -1:
    ans.append(pre[v])
    v = pre[v]
ans.reverse()
print(*ans)
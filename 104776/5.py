n = int(input())
m = int(input())
x = int(input())
y = int(input())
ans = 0
for N, M in [(x - 1, m), (n - x, m), (n, y - 1), (n, m - y)]:
    ans += (N * (N + 1) // 2) * (M * (M + 1) // 2)

for N, M in [(x - 1, y - 1), (n - x, y - 1), (x - 1, m - y), (n - x, m - y)]:
    ans -= (N * (N + 1) // 2) * (M * (M + 1) // 2)

print(ans)
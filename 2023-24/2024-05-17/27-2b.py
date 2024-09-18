import sys
sys.stdin = open('27-2b.txt')

n = int(input())

ans = 0
min_delta = 10 ** 10

for i in range(n):
    x, y = map(int, input().split())
    ans += max(x, y)
    if x % 3 != y % 3:
        min_delta = min(min_delta, abs(x - y))
if ans % 3 == 0:
    ans -= min_delta
print(ans)
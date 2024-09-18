# https://codeforces.com/contest/1843/problem/A

out = []

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(n // 2):
        ans += a[n - i - 1] - a[i]
    out.append(ans)

for i in out:
    print(i)
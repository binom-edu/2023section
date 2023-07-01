# https://codeforces.com/contest/1843/problem/C

out = []

for _ in range(int(input())):
    n = int(input())
    ans = 0
    while n:
        ans += n
        n //= 2
    out.append(ans)

for i in out:
    print(i)
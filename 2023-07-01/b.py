# https://codeforces.com/contest/1843/problem/B

out = []

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    maxs = 0
    flag = False
    ans = 0

    for i in a:
        maxs += abs(i)
        if flag and i > 0:
            flag = False
        elif not flag and i < 0:
            ans += 1
            flag = True
    out.append([maxs, ans])

for i in out:
    print(*i)
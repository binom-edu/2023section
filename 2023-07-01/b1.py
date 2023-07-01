# https://codeforces.com/contest/1843/problem/B

out = []

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    maxs = sum([abs(i) for i in a])

    for i in range(n):
        if a[i] > 0:
            a[i] = ' '
        elif a[i] == 0:
            a[i] = ''
        else:
            a[i] = '+'
    s = ''.join(a)
    out.append([maxs, len(s.split())])

for i in out:
    print(*i)
out = []
for _ in range(int(input())):
    n, k, q = map(int, input().split())
    a = [0] + [int(i) for i in input().split()]
    b = [0] + [int(i) for i in input().split()]
    n
    ans = []
    for ii in range(q):
        d = int(input())
        l, r = -1, len(a)
        while r - l > 1:
            m = (r + l) // 2
            if a[m] < d:
                l = m
            else:
                r = m
        if a[r] == d:
            ans.append(b[r])
        else:
            ans.append(b[l] + (b[r] - b[l]) * (d - a[l]) // (a[r] - a[l]))
    out.append(ans)
for i in out:
    print(*i)
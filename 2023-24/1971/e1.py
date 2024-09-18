t = int(input())
 
for _ in range(t):
    ans = []
    n, k, q = map(int, input().split())
    a = [0] + [int(i) for i in input().split()]
    b = [0] + [int(i) for i in input().split()]
    for _ in range(q):
        d = int(input())
        l, r = 0, len(a)
        while r - l > 1:
            m = (r + l) // 2
            if a[m] < d:
                l = m
            else:
                r = m
        if a[r] == d:
            ans.append(b[r])
        else:
            ans1 = b[l] + ((b[r] - b[l]) * (d - a[l])) // (a[r] - a[l])
            ans.append(ans1)
    print(*ans)
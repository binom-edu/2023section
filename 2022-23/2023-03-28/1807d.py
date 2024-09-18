out = []
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    pre = [0]
    for i in a:
        pre.append(pre[-1] + i)
    sm = pre[-1]
    for i in range(q):
        l, r, k = map(int, input().split())
        l -= 1
        r -= 1
        if (sm - (pre[r + 1] - pre[l]) + k * (r - l + 1)) % 2 != 0:
            out.append('yes')
        else:
            out.append('no')

for i in out:
    print(i)
out = []
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if n == 1:
        out.append(a[0])
        continue
    ans = a[0] + a[1] - 1
    for i in range(2, n):
        ans = ans + a[i] - 1
    out.append(ans)
for i in out:
    print(i)
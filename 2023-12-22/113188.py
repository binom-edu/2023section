n, at = map(int, input().split())
pos = []
neg = []
for i in range(n):
    x, y = map(int, input().split())
    if y >= 0:
        pos.append([x, y, i + 1])
    else:
        neg.append([x, y, i + 1])
pos.sort(key=lambda x: x[0])
neg.sort(key=lambda x: -x[1])
ans = []
for i in pos:
    if i[0] <= at:
        at += i[1]
        ans.append(i[2])
    else:
        break
for i in neg:
    if i[0] <= at:
        at += i[1]
        ans.append(i[2])
print(len(ans))
print(*ans)
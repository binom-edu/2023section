n = int(input())
a = [int(i) for i in input().split()]

cur = []
ans = [-1, -1, -1]
gameOn = False

for i in range(n):
    if a[i] < 5:
        if gameOn:
            cur[1] = i
            cur[2] += 5 - a[i]
        else:
            cur = [i, i, 5 - a[i]]
            gameOn = True
        if cur[2] > ans[2]:
            ans = cur.copy()
    else:
        if gameOn:
            gameOn = False

print(ans[0] + 1, ans[1] + 1, ans[2])
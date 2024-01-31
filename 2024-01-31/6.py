with open('3.txt') as fin:
    s = fin.read()

ans = 0
cur = 0
for i in s:
    if i == 'X':
        cur += 1
        ans = max(ans, cur)
    else:
        cur = 0
print(ans)
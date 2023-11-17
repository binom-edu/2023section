cnt = 0
for i in range(100001, 900009 + 1):
    if i % 7 + i % 10 == 10 and i % 11 == 0 and i % 55 != 0:
        cnt += 1
        maxx = i

print(maxx, cnt)
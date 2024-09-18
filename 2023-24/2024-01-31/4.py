ans = 0
for s in open('2.txt'):
    if s.count('K') > s.count('U'):
        ans += 1
print(ans)
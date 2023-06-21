s = input()
cnt = 0
s1 = ''

for c in s:
    if c == 'a':
        s1 += 'b'
        cnt += 1
    else:
        s1 += c

print(s1)
print(cnt)
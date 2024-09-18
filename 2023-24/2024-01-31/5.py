with open('3.txt') as fin:
    s = fin.read()

ans = 0
while 'X' * ans in s:
    ans += 1
print(ans - 1)
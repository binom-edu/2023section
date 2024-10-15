out = []
for _ in range(int(input())):
    n = int(input())
    s = input()
    if int(n ** 0.5) ** 2 != n:
        out.append('no')
        continue
    r = int(n ** 0.5)
    res = 'yes'
    for i in range(r):
        s1 = s[r * i : r * (i + 1)]
        if i == 0 or i == r - 1:
            if s1.count('1') != r:
                res = 'no'
        else:
            if s1.count('1') != 2 or s1[0] != '1' or s1[-1] != '1':
                res = 'no'
    out.append(res)

for i in out:
    print(i)
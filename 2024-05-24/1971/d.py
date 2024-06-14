out = []
for _ in range(int(input())):
    s = input()
    if s.count('0') == 0 or s.count('1') == 0:
        out.append(1)
    else:
        res = s.count('10') + 1
        if s.count('01') > 1:
            res += s.count('01') - 1
        out.append(res)
for i in out:
    print(i)
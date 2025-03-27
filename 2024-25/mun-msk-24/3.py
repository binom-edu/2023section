n = int(input())
ans = ''
suf = 0
for _ in range(n):
    s = input()
    if len(s) > len(ans) + suf:
        ans = s
        suf = 0
    elif len(s) == len(ans) + suf:
        if s >= ans + '0' * suf:
            ans = s
            suf = 0
        else:
            ans, suf = s, 1
    else:
        if not ans.startswith(s):
            suf = len(ans) + suf - len(s)
            if s + '0' * suf < ans:
                suf += 1
            ans = s
print(ans + '0' * suf)
            
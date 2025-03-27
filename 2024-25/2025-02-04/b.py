def is_valid(s):
    c1 = cp = 0
    for i in range(len(s)):
        if s[i] == '1':
            c1 += 1
        elif s[i] in p:
            cp += 1
    return c1 == len(s) - 1 and cp == 1

def less(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == '0':
            return 0
        if s[i] != '1':
            ans = len([j for j in p if j < s[i]])
            ans += 4 * (n - i - 1)
            if s[i] in p:
                for j in range(i + 1, n):
                    if s[j] == '0':
                        break
                    elif s[j] > '1':
                        ans += 1
                        break
            break
    return ans

l = input()
r = input()
ln = len(l)
rn = len(r)
p = ['2', '3', '5', '7']
if ln != rn:
    ans = 4 * ln - less(l)
    for k in range(ln + 1, rn):
        ans += 4 * k
    ans += less(r)
    if is_valid(r):
        ans += 1
else:
    ans = less(r) - less(l)
    if is_valid(r):
        ans += 1
print(ans)
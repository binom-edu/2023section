def divs(n):
    i = 2
    ans = set()
    while i ** 2 <= n:
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
        i += 1
    return ans
def m(n):
    s = divs(n)
    if s:
        return sum(s) // len(s)
    return 0

cnt = 0
n = 550000 + 1
while cnt < 5:
    if m(n) % 31 == 13:
        print(n, m(n))
        cnt += 1
    n += 1
    
def f(n):
    ans = 3 * n
    if n > 1:
        ans += n - 2
        ans += f(n - 1)
        ans += f(n - 2)
    return ans

n = 1
while f(n) < 450000:
    n += 1
print(n, f(n))

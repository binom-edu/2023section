def F(n):
    global ans
    ans += 1
    if n >= 1:
        ans += 1
        F(n-1)
        F(n-2)

ans = 0
F(28)
print(ans)
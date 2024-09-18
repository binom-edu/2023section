ans = 0

def prime(n):
    global ans
    if n == 1:
        return
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return
        d += 1
    ans += 1
    # print(n)

for i in range(1, 101):
    prime(i)
print(ans)
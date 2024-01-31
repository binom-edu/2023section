n = int(input())
m = int(input())
ans = 1
if n > 0:
    ans *= 2 * n
if m > 0:
    ans *= (m + 1)
print(ans)
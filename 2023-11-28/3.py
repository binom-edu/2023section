def f(n):
    s = bin(n)[2:]
    s1 = int(s[1:], 2)
    return n - s1

ans = set()
for i in range(500, 5000+1):
    ans.add(f(i))

print(len(ans))
print(ans)
def f(n):
    ans = 0
    while n != 0:
        ans += n % 10
        n //= 10
    return ans

import random
n = 10
a = [random.randint(0, 1000) for i in range(10)]
print(a)

ans = None
summ = 0
for i in a:
    if f(i) > summ:
        ans = i
        summ = f(i)
print(ans)
print(max(a, key=f))

print(max(a, key=lambda x: sum(map(int, str(x)))))
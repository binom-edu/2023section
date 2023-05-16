import random
n = 10
a = [random.randint(-100, 100) for i in range(n)]

print(*a)

b = sorted(a)
print(*a)
print(*b)

a.sort()
print(*a)
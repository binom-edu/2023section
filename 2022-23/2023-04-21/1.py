import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print(*a)

b = [1, 2]

a.extend(b)

print(a)
import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print(*a)

print(a[-1])
import random

n = 15
a = [random.randint(0, 100) for i in range(n)]
print(a)

a.sort(reverse=True)
print(a)
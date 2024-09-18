import random
n = 10
a = [random.randint(0, 10) for i in range(10)]
print(a)

print(all(i > 0 for i in a))
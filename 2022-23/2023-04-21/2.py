import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print(*a)

a.insert(1, 777)
print(a)
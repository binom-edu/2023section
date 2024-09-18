import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print('a:', a)

b = a.copy()

print('b:', b)

b[0] = 777
print('a:', a)
print('b:', b)
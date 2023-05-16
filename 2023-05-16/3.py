# упорядочим массив по последней цифре элементов

def f(x):
    return abs(x) % 10

import random
n = 10
a = [random.randint(-100, 100) for i in range(n)]

print(*a)

a.sort(key=f)
print(*a)

a.sort(key=lambda x: abs(x) % 10)
print(*a)
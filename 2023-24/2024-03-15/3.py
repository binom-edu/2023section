from functools import reduce

def f(a, b):
    if a > b:
        return a
    return b

import random
n = 10
a = [random.randint(0, 1000) for i in range(10)]
print(a)

print(reduce(f, a))
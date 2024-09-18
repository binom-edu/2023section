# Сортировка пузырьком

import random
n = 10
a = [random.randint(0, 100) for i in range(n)]

print(*a)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j + 1] < a[j]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a)
# Сортировка выбором

import random
n = 10
a = [random.randint(0, 100) for i in range(n)]

print(*a)

for i in range(n - 1):
    jmin = i
    for j in range(i + 1, n):
        if a[j] < a[jmin]:
            jmin = j
    a[i], a[jmin] = a[jmin], a[i]

print(*a)
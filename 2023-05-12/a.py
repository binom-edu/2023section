import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]
print(*a)

def qSort(a, l, r):
    if l >= r:
        return
    i, j = l, r
    x = a[(l + r) // 2]
    while i <= j:
        while a[i] < x: i += 1
        while a[j] > x: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1; j -= 1
    qSort(a, l, j)
    qSort(a, i, r)

qSort(a, 0, n // 2 - 1)
qSort(a, n // 2 + 1, n - 1)
print(*a)
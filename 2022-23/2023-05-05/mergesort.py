import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]
print(*a)

def merge(a, b):
    c = []
    while a and b:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    c += a + b
    return c

def mergeSort(a):
    if len(a) < 2:
        return a
    m = len(a) // 2
    b = mergeSort(a[:m])
    c = mergeSort(a[m:])
    return merge(b, c)

a = mergeSort(a)
print(*a)
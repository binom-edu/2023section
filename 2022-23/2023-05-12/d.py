import random
n = 10
a = [3, 2, 1, 0, 4, 5, 6, 7, 8, 9]

def qSort(a, l, r):
    global cnt # количество перестановок
    if l >= r:
        return
    i, j = l, r
    x = a[(l + r) // 2]
    while i <= j:
        while a[i] < x: i += 1
        while a[j] > x: j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            cnt += 1
            i += 1; j -= 1
    qSort(a, l, j)
    qSort(a, i, r)

def bubbleSort(a):
    global cnt
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j + 1] < a[j]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cnt += 1

def selectionSort(a):
    global cnt
    for i in range(n - 1):
        jmin = i
        for j in range(i + 1, n):
            if a[j] < a[jmin]:
                jmin = j
                cnt += 1
        a[i], a[jmin] = a[jmin], a[i]

# сортировка пузырьком
cnt = 0
bubbleSort(a)
print('bubbleSort:', cnt)

# быстрая сортировка
cnt = 0
qSort(a, 0, n - 1)
print('qSort:', cnt)
import random, time

def isOrdered(a: list):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

def bogoSort(a):
    while not isOrdered(a):
        random.shuffle(a)

def foolSort(a):
    n = len(a)
    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            i = 0
        else:
            i += 1

def bubbleSort(a):
    for i in range(n - 1):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]

def bubbleSort1(a):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]

n = 1000
a = [random.randint(0, 100) for i in range(n)]
b = a.copy()
c = a.copy()
d = a.copy()

# start = time.time()
# bogoSort(a)
# if isOrdered(a):
#     print('bogo:', time.time() - start)

start = time.time()
foolSort(b)
if isOrdered(b):
    print('fool:', time.time() - start)

start = time.time()
bubbleSort(c)
if isOrdered(c):
    print('bubble:', time.time() - start)

start = time.time()
bubbleSort1(d)
if isOrdered(d):
    print('bubble1:', time.time() - start)

import random

def isOrdered(a: list):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True

n = 15
a = [random.randint(0, 100) for i in range(n)]
print(a)

while not isOrdered(a):
    random.shuffle(a)

print(a)
import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print(a)

if 2 in a:
    print(a.index(2))
else:
    print('не найдено')
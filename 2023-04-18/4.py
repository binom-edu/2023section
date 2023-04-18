import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]

print(a)

x = a.pop() # удаляет элемент с указанным индексом (по умолчанию последний) и возвращает его
print(x)
print(a)
print(a.pop(1))
print(a)
# создание списка
a = []
for i in range(10):
    a.append(i)

print(a)

b = [i for i in range(10)]
c = [i ** 2 for i in range(10)]
d = [i ** 2 for i in range(10) if i ** 2 % 10 == 9]
print(b)
print(c)
print(d)
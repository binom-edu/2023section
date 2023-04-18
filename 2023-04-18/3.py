import random
n = 10
a = [random.randint(-10, 10) for i in range(n)]

print(a)

# сколько в списке положительных элементов?
ans = 0
for i in range(n):
    if a[i] > 0: # i -- индекс элемента, что-то делаем с a[i]
        ans += 1

print(ans)

ans = 0
for i in a:
    if i > 0: # i -- сам элемент, что-то делаем с i
        ans += 1
print(ans)

positive = [i for i in a if i > 0]
print(positive)
print(len(positive))
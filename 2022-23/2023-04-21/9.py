import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print('a:', a)

ans = 0
sum_neg = 0
for i in a:
    if i < 0:
        ans += 1 # считаем количество отрицательных элементов
        sum_neg += i # сумма отрицательных элементов
print(ans)
print(sum_neg)
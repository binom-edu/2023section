import random
n = 10
a = [random.randint(-20, 20) for i in range(n)]

print('a:', a)

# количество пар элементов с четной суммой
ans = 0

for i in range(n - 1):
    if (a[i] + a[i + 1]) % 2 == 0:
        ans += 1

print(ans)
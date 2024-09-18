# сумма цифр числа
n = int(input())
n1 = n
ans = 0
while n1 > 0:
    ans += n1 % 10
    n1 //= 10
print(f'Сумма цифра чилса {n} равна {ans}')
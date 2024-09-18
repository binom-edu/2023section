def print10():
    print('*' * n) # в функции можно использовать глобальные переменные
    print()

n = 10 # глобальная переменная
print10()
n = 15
print10()

for n in range(10):
    print10()
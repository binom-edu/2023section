# алгоритм Евклида 2
a = int(input())
b = int(input())
while a * b != 0:
    if a > b:
        a %= b
    else:
        b %= a

print(a + b)
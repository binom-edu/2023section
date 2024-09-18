# алгоритм Евклида 1
a = int(input())
b = int(input())
while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)
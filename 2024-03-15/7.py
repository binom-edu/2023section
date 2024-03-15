# (ДЕЛ(x, 7) → ¬ДЕЛ(x, 5)) \/ (x + A ≥ 80)

def f(x, a):
    return x % 7 != 0 or x % 5 != 0 or x + a >= 80

a = 1
while not all(f(x, a) for x in range(1, 100)):
    a += 1
print(a)
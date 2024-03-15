# (x ≥ 7) ⋁ (2x < y) ⋁ (x ⋅ y < A)

def f(x, y, a):
    return x >= 7 or 2 * x < y or x * y < a

a = -50
while not all(f(x, y, a) for x in range(1, 100) for y in range(1, 100)):
    a += 1
print(a)
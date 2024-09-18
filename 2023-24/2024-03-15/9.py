# (( (X & 13 ≠ 0) ∨ (X & A = 0)) → (X & 13 ≠ 0)) ∨ (X & A ≠ 0) ∨ (X & 39 = 0)

def f(x, a):
    return not (x & 13 != 0 or x & a == 0) or x & 13 != 0 or x & a != 0 or x & 39 == 0

ans = 0
for a in range(1, 100):
    if all(f(x, a) for x in range(1, 100)):
        ans = a
        break
print(ans)
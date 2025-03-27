a = int(input())
b = int(input())

if b < a + 2 or (b - a - 2) % 2 != 0:
    print(-1)
    exit(0)
l = (b - a - 2) // 2
if a - 1 < l + 2:
    print(-1)
    exit(0)
r = a - l - 3
if r % 2 == 0:
    print(l + r // 2 + 2)
else:
    print(-1)
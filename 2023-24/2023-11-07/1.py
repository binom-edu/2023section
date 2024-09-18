# черепаха
from math import *
ang = radians(30)
ans = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if y < tan(ang) * x and y > -tan(ang) * x \
            and x < cos(ang) * 10:
            ans += 1
print(ans)
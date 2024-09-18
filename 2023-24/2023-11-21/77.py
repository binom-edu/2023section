cnt = 0
ans = 0
a = []
for x in range(2020, 647038 + 1):
    digits = [int(i) for i in str(x)]
    mind = min(digits)
    sumd = sum(digits)
    if sumd < 10 and not (str(mind) in str(x)[:3]):
        a.append(x)

avg = sum(a) / len(a)
for i in a:
    if abs(i - avg) < abs(ans - avg):
        ans = i
print(len(a), ans)
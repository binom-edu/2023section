import itertools

alf = sorted('школа')

ans = 0
for num, i in enumerate(itertools.product(alf, repeat=4)):
    s = ''.join(i)
    if 'лол' in s:
        print(num)
        break

print(ans)
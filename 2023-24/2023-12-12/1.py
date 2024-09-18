a = '123x5'
b = '1x233'

alf = '0123456789abcdef'
for x in alf:
    res = int(a.replace('x', x), 15) + int(b.replace('x', x), 15)
    if res % 14 == 0:
        print(res // 14)
        break

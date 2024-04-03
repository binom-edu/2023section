import itertools

alf = sorted('кланпечь')

for num, i in enumerate(itertools.product(alf, repeat=8)):
    s = ''.join(i)
    if s == 'печалька':
        c = num
    if s == 'печенька':
        print(num - c - 1)
        break
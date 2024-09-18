def lower_bound(a, x):
    '''возвращает наименьший индекс элемента в массиве a, который меньше либо равен x'''
    n = len(a)
    l, r = -1, n
    while r - l > 1:
        m = (r + l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    return r

a = [2, 4, 5, 5, 7, 13, 21, 23]
x = 5
ans = lower_bound(a, x)
if ans == len(a) or a[ans] != x:
    print(-1)
else:
    print(ans)
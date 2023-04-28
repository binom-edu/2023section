def isSorted(a):
    '''Проверка упорядоченности списка'''
    for i in range(len(a) - 1):
        if a[i + 1] < a[i]:
            return False
    return True

print(isSorted([1, 2, 3]))
print(isSorted([2, 3, 1]))
def f(n):
    '''считает n-е число Фибоначчи'''
    if n < 2: # терминальное условие
        return n
    return f(n - 1) + f(n - 2)

n = int(input())
print(f(n))
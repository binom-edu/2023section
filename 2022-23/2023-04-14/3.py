def f(n):
    '''печатает двоичный код n'''
    if n == 0:
        return
    f(n // 2)
    print(n % 2, end='')

f(6)
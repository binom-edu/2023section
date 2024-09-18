def countOfDigits(n: int) -> int:
    '''Подсчитывает количество цифр числа'''
    ans = 0
    while n:
        ans += 1
        n //= 10
    return ans

def isAutomorph(n: int) -> bool:
    return n ** 2 % (10 ** countOfDigits(n)) == n


a, b = map(int, input().split())

flag = True
for i in range(a, b + 1):
    if isAutomorph(i):
        flag = False
        print(i, end=' ')

if flag:
    print(-1, end=' ')

print()
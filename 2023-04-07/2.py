def isPrime(n):
    if n == 1:
        return False
    d = 2
    while d ** 2 <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print(isPrime(8))
print(isPrime(17))

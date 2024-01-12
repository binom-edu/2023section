def last_digit(n):
    return abs(n) % 10

def sum_of_digits(n):
    ans = 0
    while n > 0:
        ans += last_digit(n)
        n //= 10
    return ans

n = int(input())
print(sum_of_digits(n))
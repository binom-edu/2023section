import functools
import sys

sys.setrecursionlimit(10**6)

@functools.lru_cache(1000)
def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)

n = int(input())
print(f(n))
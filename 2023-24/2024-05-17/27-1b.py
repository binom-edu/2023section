import sys
sys.stdin = open('27-1b.txt')

n = int(input())

n1 = n2 = n13 = n26 = 0
for i in range(n):
    x = int(input())
    if x % 26 == 0:
        n26 += 1
    elif x % 13 == 0:
        n13 += 1
    elif x % 2 == 0:
        n2 += 1
    else:
        n1 += 1

print(n26 * (n26 - 1) // 2 + n26 * (n - n26) + n2 * n13)
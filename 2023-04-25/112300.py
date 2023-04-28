n = int(input())
a = [int(i) for i in input().split()]
r = int(input())

b = [0] * n
for i in range(n):
    b[i] = a[(i + r) % n]

print(*b)
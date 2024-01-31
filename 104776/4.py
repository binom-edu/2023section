n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
p = int(input())

step = 0
k = 1
for i in range(n - 2, -1, -1):
    step += a[i] * k
    k += 1
print((p - sum(a)) // step)
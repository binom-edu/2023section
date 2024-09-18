import sys
sys.stdin = open('27-1a.txt')

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] * a[j] % 26 == 0:
            ans += 1
print(ans)
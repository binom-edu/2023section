import sys
sys.stdin = open('26-1.txt')

s, n = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

a.sort()
b = []
for i in a:
    if sum(b) + i <= s:
        b.append(i)

print(len(b))
b.pop()

delta = s - sum(b)
print(max([i for i in a if i <= delta]))
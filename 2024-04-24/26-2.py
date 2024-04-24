import sys
sys.stdin = open('26-2.txt')

n, k = map(int, input().split())
a = []
for i in range(n):
    weight, price = map(int, input().split())
    a.append([weight, price])

a.sort(key=lambda x: [x[1] / x[0], -x[0]])
b = a[:k]
print(sum([i[0] for i in b]))
print(max(b)[1])
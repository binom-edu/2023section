# чтение двумерного списка с клавиатуры
n, m = map(int, input().split())

a = []

for i in range(n):
    buf = [int(j) for j in input().split()]
    a.append(buf)

for i in a:
    print(*i)
import sys
sys.stdin = open('26.txt')

n = int(input())
events = []
for i in range(n):
    x, y = map(int, input().split())
    events.append([x, y])
events.sort()

end = cnt = 0
for event in events:
    if event[0] >= end:
        cnt += 1
        prev = end
        end = event[1]
    elif event[1] < end:
        end = event[1]

print(cnt)
ans = 0
for event in events:
    if event[0] >= prev:
        ans = max(ans, event[1])
print(ans)

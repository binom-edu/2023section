out = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    if b % 2 == 0:
        if a % 2 == 0:
            out.append('yes')
        else:
            out.append('no')
    else:
        if a > 1 and a % 2 == 0:
            out.append('yes')
        else:
            out.append('no')
for i in out:
    print(i)
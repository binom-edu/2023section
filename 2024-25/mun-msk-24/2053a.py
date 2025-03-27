for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(n - 1):
        x, y = a[i], a[i + 1]
        if x > y:
            x, y = y, x
        if y < x * 2:
            print('YES')
            break
    else:
        print('NO')
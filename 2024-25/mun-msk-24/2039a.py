for _ in range(int(input())):
    n = int(input())
    print(*(i * 2 - 1 for i in range(1, n + 1)))
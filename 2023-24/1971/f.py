for _ in range(int(input())):
    r = int(input())
    ans = set()
    for x in range(-r - 1, r + 2):
        y = int(abs(r ** 2 - x ** 2) ** 0.5)
        for y1 in range(y - 100, y + 101):
            if r ** 2 <= x ** 2 + y1 ** 2 < (r + 1) ** 2:
                ans.add((x, y1))
                ans.add((x, -y1))
    print(len(ans))
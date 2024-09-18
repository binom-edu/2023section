# является ли число n простым
n = int(input())
d = 2
while d < n:
    if n % d == 0:
        print('no')
        break
    d += 1
else:
    print('yes')
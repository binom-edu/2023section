a = [5, 12, 17, 4, 20]

h = 6
while any(i < h for i in a):
    h -= 1
print(h)
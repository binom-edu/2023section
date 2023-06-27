s = 0
cnt = 0
for line in open('input.txt'):
    cnt += 1
    s += int(line)

with open('output.txt', 'w') as fout:
    print(s / cnt, file=fout)
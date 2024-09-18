import fnmatch
# mask 1?5719*6
def isValid(n):
    return fnmatch.fnmatch(str(n), '1?5719*6')
    # s = str(n)
    # return s.startswith('1') and s[2:6] == '5719' and s.endswith('6')

for i in range(0, 10 ** 10 + 1, 2023):
    if isValid(i):
        print(i, i // 2023)
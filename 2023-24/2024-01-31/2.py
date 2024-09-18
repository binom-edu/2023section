import sys
old_input = sys.stdin
sys.stdin = open('1.txt')

s = input()
print(s)
s = input()
print(s)

sys.stdin = sys.__stdin__
import functools

@functools.cache
def f(s):
    if s >= 68:
        return ['-', 0]
    moves = [f(s + 1), f(s + 4), f(s * 5)]
    win = []
    lose = []
    for move in moves:
        if move[0] == '+':
            lose.append(move[1])
        else:
            win.append(move[1])
    if win:
        return ['+', min(win) + 1]
    else:
        return ['-', max(lose)]
for s in range(1, 68):
    print(s, *f(s))
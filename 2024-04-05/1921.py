import functools

@functools.lru_cache(10000)
def f(s1, s2):
    if s1 + s2 >= 77:
        return ['-', 0]
    moves = [f(s1 + 1, s2), f(s1 * 2, s2), f(s1, s2 + 1), f(s1, s2 * 2)]
    win = []
    lose = []
    for move in moves:
        if move[0] == '-':
            win.append(move[1])
        else:
            lose.append(move[1])
    if win:
        return ['+', min(win) + 1]
    return ['-', max(lose)]

for s in range(1, 70):
    print(s, *f(7, s))
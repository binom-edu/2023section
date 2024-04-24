import random, heapq

def print_board(board):
    for i in range(n):
        for j in range(n):
            print(board[i * n + j] + 1 if board[i * n + j] != n ** 2 - 1 else '_', end=' ')
        print()

def move(board, dir):
    pos = board.index(n ** 2 - 1)
    i, j = pos // n, pos % n
    if dir == 'u' and i > 0:
        board[pos], board[pos - n] = board[pos - n], board[pos]
        return True
    elif dir == 'd' and i < n - 1:
        board[pos], board[pos + n] = board[pos + n], board[pos]
        return True
    elif dir == 'l' and j > 0:
        board[pos], board[pos - 1] = board[pos - 1], board[pos]
        return True
    elif dir == 'r' and j < n - 1:
        board[pos], board[pos + 1] = board[pos + 1], board[pos]
        return True
    else:
        return False

def get_h(board):
    y, mod = 31, 10 ** 9 + 7
    ans = 0
    for i in range(n ** 2):
        ans = (ans + board[i] * y ** i) % mod
    return ans

def get_neighbours(board):
    ans = []
    for d in 'urld':
        bc = board.copy()
        if move(bc, d):
            ans.append(bc)
    return ans

def heu(v):
    ans = 0
    for i in range(len(v)):
        if i != v[i]:
            ans += 1
    return ans

n = 4
board = [i for i in range(n ** 2)]
fin = board.copy()

for i in range(100):
    move(board, random.choice('urdl'))
# random.shuffle(board)

# print_board(board)

d = dict()
q = []
heapq.heapify(q)

# q.append(board)
heapq.heappush(q, [0 + heu(board), board])
d[get_h(board)] = 0

while q:
    # v = q.pop(0)
    v = heapq.heappop(q)[1]
    h_v = get_h(v)
    if v == fin:
        cnt = d[h_v]
        break
    neighbours = get_neighbours(v)
    for u in neighbours:
        h = get_h(u)
        if not h in d or d[h] > d[h_v] + 1:
            d[h] = d[h_v] + 1
            heapq.heappush(q, [d[h] + heu(u), u])
            # q.append(u)

# Восстановление ответа    
ans = [fin]
v = fin
while v != board:
    h_v = get_h(v)
    for u in get_neighbours(v):
        if get_h(u) in d and d[get_h(u)] == d[h_v] - 1:
            v = u
            ans.append(u)
            break

ans.reverse()
for v in ans:
    print_board(v)
    print('---')
print(cnt)
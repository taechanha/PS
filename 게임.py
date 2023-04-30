

def max_moves(r, c, dir, moves, path):
    if not (0 <= r < H and 0 <= c < W):
        return moves
    if board[r][c] == 'H':
        return moves
    if (r, c) in path:
        print(-1)
        exit(0)
    if (r, c) in cache:
        return cache[(r, c)]

    mac_case = moves
    for i in range(4):
        times = board[r][c]
        path.add((r, c))
        mac_case = max(mac_case, max_moves(
            r + times*dr[i], c + times*dc[i], i, moves+1, path))
        path.remove((r, c))

    cache[(r, c)] = mac_case
    return cache[(r, c)]


H, W = map(int, input().split())
board = [list(map(lambda c: c if c == 'H' else int(c), input()))
         for _ in range(H)]
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
cache = {}
res = max_moves(0, 0, "dir", 0, set())
print(-1 if res == float('inf') else res)


# 10 10
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111
# 1111111111

import sys
sys.setrecursionlimit(10**7)

def oob(r, c):
    return not (0 <= r < m and 0 <= c < n)

def max_moves(r, c, mov):
    global max_mov
    max_mov = max(max_mov, mov)
    next_moves = mov+1
    for i in range(4):
        nr = dr[i] * int(board[c][r]) + r
        nc = dc[i] * int(board[c][r]) + c
        if oob(nr, nc):
            continue
        if board[nc][nr] == -1:
            continue
        if (nc, nr) in cache and next_moves <= cache[(nc, nr)]:
            continue
        if visit[nc][nr]:
            print(-1)
            exit(0)
        cache[(nc, nr)] = next_moves
        visit[nc][nr] = True
        max_moves(nc, nr, next_moves)
        visit[nc][nr] = False

n, m = map(int, input().split())
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
board = [list(map(lambda c: -1 if c == 'H' else int(c), input()))
         for _ in range(H)]
cache = dict()
visit = [[False for _ in range(m)] for __ in range(n)]
max_mov = 1
max_moves(0, 0, 0)
print(max_mov)
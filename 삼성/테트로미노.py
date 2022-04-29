def search(i, j):
    global max_cnt, tetrominos
    for tetromino in tetrominos:
        cnt = 0
        for r, c in tetromino:
            nr = i + r
            nc = j + c
            if not (0 <= nr < n and 0 <= nc < m):
                break
            cnt += board[nr][nc]
        else:
            max_cnt = max(max_cnt, cnt)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
tetrominos = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    #
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    #
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    #
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (1, 1), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    #
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
]

for i in range(n):
    for j in range(m):
        search(i, j)

print(max_cnt)
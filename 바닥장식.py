# 6:42 ~

# 4 4
# ----
# ----
# ----
# ----

def rotate_cw_90(board):
    return list(zip(*board[::-1]))


n, m = map(int, input().split())
board = [input() for _ in range(n)]

kinds = [0, 0]

for i in range(n):
    cnt = 0
    for j in range(m-1):
        if board[i][j] != '-':
            continue
        if board[i][j] != board[i][j+1]:
            cnt += 1
    if board[i][-1] == '-':
        cnt += 1
    kinds[0] += cnt
    # print(cnt)

board = rotate_cw_90(board)

for i in range(m):
    cnt = 0
    for j in range(n-1):
        if board[i][j] != '|':
            continue
        if board[i][j] != board[i][j+1]:
            cnt += 1
    if board[i][-1] == '|':
        cnt += 1
    kinds[1] += cnt
    # print(cnt)

print(sum(kinds))

# 완전탐색. 결국 모든 CCTV 조합에 대해 탐색하면 끝

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctvs = []

for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            # kind, r, c
            cctvs.append((board[i][j], i, j))

def get_blind_spots(board):
    return sum([row.count(0) for row in board])

def dfs(i):
    global board, cctvs, r, c, min_cnt
    if i >= len(cctvs):
        cnt = get_blind_spots(board)
        min_cnt = min(min_cnt, cnt)
        return

    for dir in range(4):
        temp_board = [row[:] for row in board]
        kind, r, c = cctvs[i]
        search(kind, dir)
        dfs(i+1)
        board = [row[:] for row in temp_board]

# kind: 1, 2, 3, 4, 5
def search(kind, dir):
    global board, r, c
    # kind, r, c
    if kind == 1:
        if dir == 0:  # 위
            left()
        elif dir == 1:  # 오른
            right()
        elif dir == 2:  # 아래
            down()
        elif dir == 3:  # 왼
            up()
    elif kind == 2:  # < >
        if dir == 0:
            right()
            left()
        elif dir == 1:
            up()
            down()
        else:
            return
    elif kind == 3:  # ^ >
        if dir == 0:
            up()
            right()
        elif dir == 1:
            right()
            down()
        elif dir == 2:
            down()
            left()
        else:
            left()
            up()
    elif kind == 4:  # < ^ >
        if dir == 0:
            left()
            up()
            right()
        elif dir == 2:
            up()
            right()
            down()
        elif dir == 3:
            right()
            down()
            left()
        else:
            down()
            left()
            up()
    else:  # < ^ / >
        up()
        right()
        down()
        left()


def left():
    global board, r, c
    for i in range(c-1, -1, -1):
        if board[r][i] == 0:
            board[r][i] = '#'
        elif board[r][i] == 6:
            break


def right():
    global board, m, r, c
    for i in range(c+1, m):
        if board[r][i] == 0:
            board[r][i] = '#'
        elif board[r][i] == 6:
            break


def up():
    global board, r, c
    for i in range(r-1, -1, -1):
        if board[i][c] == 0:
            board[i][c] = '#'
        elif board[i][c] == 6:
            break


def down():
    global board, n, r, c
    for i in range(r+1, n):
        if board[i][c] == 0:
            board[i][c] = '#'
        elif board[i][c] == 6:
            break

min_cnt = float('inf')
dfs(0)
print(min_cnt)

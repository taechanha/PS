def move_board(dir):
    global board, ops
    for op in ops[dir]:
        if op == 'move':
            move_left()
        else:
            for _ in range(op):
                board = rotate_cw_90(board)


def move_left():
    global board
    for i in range(len(board)):
        # 모든 row에 대해 merge & go
        gravitate(board[i]) # |
        merge(board[i])     # |  실수 1 
        gravitate(board[i]) # |


def merge(row):
    for i in range(1, len(row)):
        if row[i] == row[i-1]:
            row[i-1] = row[i] + row[i-1]
            row[i] = 0


def gravitate(row):
    for i in range(len(row)):
        if row[i] == 0:
            for j in range(i+1, len(row)):
                if not row[j] == 0:
                    row[i] = row[j]
                    row[j] = 0
                    break


def rotate_cw_90(board) -> list[list[int]]:
    n = len(board)
    m = len(board[0])
    temp = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            temp[c][n-1-r] = board[r][c]
    return temp


def dfs(dir, step):
    global board, max_block
    if step == 5:
        cur_max_block = max(map(max, board))
        max_block = max(max_block, cur_max_block)
        return
    # 왼오위아
    for dir in range(4):
        # choose
        temp_board = [row[:] for row in board]
        # explore
        move_board(dir)
        dfs(dir, step+1)
        # un-choose
        board = [row[:] for row in temp_board]


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
ops = dict()
ops[0] = ['move']  # 왼:  연산
ops[1] = [2, 'move', 2]  # 오른: 회전2 - 연산 - 회전2
ops[2] = [3, 'move', 1]  # 위: 회전3 - 연산 - 회전1
ops[3] = [1, 'move', 3]  # 아래: 회전1 - 연산 - 회전3

max_block = 0
dfs(0, 0)
print(max_block)

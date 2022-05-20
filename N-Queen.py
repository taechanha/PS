import time
n = int(input())
board = [[0] * n for _ in range(n)]
cnt = 0

ret = []

debug = 1


def rec(row):
    global board, cnt
    if row == n:
        if debug:
            ret.append([row[:] for row in board])
        cnt += 1
        return

    # 놓을 수 있으면 놓기
    for col in range(n):
        # 위에 없고, 왼쪽 대각선 위에 없고, 오른쪽 대각선 위에 없으면
        if up(row, col) and left_up(row, col):  # and right_up(row, col):
            board[row][col] = 'Q'
            rec(row+1)
            board[row][col] = 0


def up(row, col):
    for r in range(row):
        if board[r][col] == 'Q':
            return False
    return True


def left_up(row, col):
    for i in range(row, 0, -1):
        if 0 <= col-i < n:
            if board[row-i][col-i] == 'Q':
                return False

        if 0 <= col+i < n:
            if board[row-i][col+i] == 'Q':
                return False
    return True


# def right_up(row, col):
#     for i in range(row, 0, -1):
#         if not (0 <= row-i < n and 0 <= col+i < n):
#             continue
#         if board[row-i][col+i] == 'Q':
#             return False
#     return True

if debug:
    s = time.time()
rec(0)
print(cnt)
if debug:
    print(time.time() - s)

# if debug:
#     for each in ret:
#         for row in each:
#             print(row)
#         print()

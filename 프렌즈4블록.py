def is_fang(r, c, board) -> bool:
    if board[r][c] == board[r+1][c]\
            and board[r][c] == board[r+1][c+1]\
            and board[r][c] == board[r][c+1]:
        return True

    return False


def set_fang(list_to_fang: list, board):
    while list_to_fang:
        r, c = list_to_fang.pop()
        board[r][c] = '#'


def drop_block(board):
    m = len(board)
    n = len(board[0])
    
    for c in range(n):
        for r in range(m-1, -1, -1):
            # print(r, c)
            if board[r][c] == '#':
                # 현재는 참
                temp_r = r
                fl = 0
                while board[temp_r][c] == '#':
                    if temp_r == 0:
                        fl = 1
                        break
                    temp_r -= 1

                # board[temp_r][c] == '#' and temp_r == 0
                if fl == 1:
                    # do nothing
                    pass
                # board[temp_r][c] != '#'
                else:
                    board[r][c] = board[temp_r][c]
                    board[temp_r][c] = '#'


def count_fang(board) -> int:
    return sum([row.count('#') for row in board])


def convert_to_list(s: str) -> list:
    return [list(row) for row in s]


def fill_list(r, c):
    return [[r, c], [r+1, c], [r+1, c+1], [r, c+1]]

def set_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '#':
                board[i][j] = '@'

def solution(m, n, board):
    """
    m: rows
    n: cols
    """
    cnt = 0

    board = convert_to_list(board)
    list_to_fang = []

    # search thru board
    # kernel
    while True:
        more_game = 0
        for r in range(m - 1):
            # 0, 1, 2 | m-1: 3
            for c in range(n - 1):
                # 0, 1, 2, 3 | n-1: 4
                if board[r][c] == '@':
                    continue
                if is_fang(r, c, board):
                    list_to_fang += fill_list(r, c)
                    more_game = 1

        if more_game == 0:
            break
        set_fang(list_to_fang, board)
        drop_block(board)
        cnt += count_fang(board)
        set_empty(board)

    return cnt


m = 4
n = 5
board = ["CCBDE",
         "AAADE",
         "AAABF",
         "CCBBF"]
# -----------------------         
m = 6
n = 6         
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

res = solution(m, n, board)

print(res)

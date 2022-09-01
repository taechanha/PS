from collections import defaultdict
r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
time = 0


def rotate_90_cw(board):
    return [list(reversed(row)) for row in zip(*board)]


def rotate_90_ccw(board):
    return [list(row) for row in zip(*reversed(board))]


while time <= 100:

    # 종료조건
    if 0 <= r-1 < len(board) and 0 <= c-1 < len(board[0]):
        if board[r-1][c-1] == k:
            print(time)
            exit()

    time += 1

    temp_board = []
    max_len = 0
    # R 연산
    if len(board) >= len(board[0]):
        for row in board:
            counter = defaultdict(int)
            # construct counter
            for each in row:
                # 0은 제외
                if each == 0:
                    continue
                counter[each] += 1

            # operation
            # result: [[2, 1], [1, 2]]
            temp_row = []
            result = [[each, counter[each]]
                      for each in sorted(counter, key=lambda x: (counter[x], x))]

            # preprocess
            # temp_row: [2, 1, 1, 2]
            for each in result:
                temp_row += each

            # construct temp board
            max_len = max(max_len, len(temp_row))
            temp_board.append(temp_row)

        # append 0s
        for i, row in enumerate(temp_board):
            temp_board[i] += [0] * (max_len - len(row))

        # 초기화
        board = [row[:] for row in temp_board]

    # C 연산
    else:
        board = rotate_90_cw(board)

        temp_board = []
        max_len = 0
        for row in board:
            counter = defaultdict(int)
            # construct counter
            for each in row:
                # 0은 제외
                if each == 0:
                    continue
                counter[each] += 1

            # operation
            # result: [[2, 1], [1, 2]]
            temp_row = []
            result = [[each, counter[each]]
                      for each in sorted(counter, key=lambda x: (counter[x], x))]

            # preprocess
            # temp_row: [2, 1, 1, 2]
            for each in result:
                temp_row += each

            # construct temp board
            max_len = max(max_len, len(temp_row))
            temp_board.append(temp_row)

        for i, row in enumerate(temp_board):
            temp_board[i] = list(reversed(row))

        # append 0s
        for i, row in enumerate(temp_board):
            temp_board[i] = [0] * (max_len - len(row)) + temp_board[i]

        temp_board = rotate_90_cw(rotate_90_cw(rotate_90_cw(temp_board)))

        # 초기화
        board = [row[:] for row in temp_board]

if time > 100:
    print(-1)
else:
    print(time)

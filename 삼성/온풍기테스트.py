def is_in_boundary(r, c):
    return 0 <= r < R and 0 <= c < C


def distribute_temparature(board, r, c):

    copy_board = [[0] * C for _ in range(R)]
    cnt = 5
    stack = [(r, c+1, cnt)]
    visited = [(r, c+1)]

    while stack:
        r, c, cnt = stack.pop()
        copy_board[r][c] = cnt
        # try:
        #     copy_board[r][c] = cnt
        # except:
        #     print(r, c, len(copy_board), len(copy_board[0]))

        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[0]

            if not is_in_boundary(nr, nc):
                continue
            if (nr, nc) in visited:
                continue
            if (nr, nc) in wall_from_right:
                continue

            stack.append((nr, nc, cnt-1))
            visited.append((nr, nc))

    print(copy_board)


# =================================== #
R, C = 9, 6
board = [[0] * C for _ in range(R)]
wall_from_right = [(3-1, 5-1)]  # [(4, 4)]
heater_r = 3 - 1
heater_c = 1 - 1
dr = [0, -1, 1]
dc = [1]

distribute_temparature(board, heater_r, heater_c)


# 4 4 1
# 5 4 0
# 5 6 0

# 이 정보는 세 정수 x, y, t로 이루어져 있다.
# t가 0인 경우 (x, y)와 (x-1, y) 사이에 벽이 있는 것이고,
# 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽이 있는 것이다.

#
# 4 4 1 -> (3, 4) | (4, 4) -> 하=>상 일 때 (3, 4) 못가고 상=>하 일 때 (4, 4) 못 감
# 5 4 0 -> (5, 4) | (5, 5) -> 좌=>우 일 때 (5, 5) 못가고 우=>좌 일 때 (5, 4) 못 감
#
# 그냥 dfs 중에 (r, c), (nr, nc) 보고 판단하면 되나?
#
#
#
#
#
#
#
#
#

[[0, 0, 0, 3, 2, 1],
 [0, 0, 4, 3, 2, 1],
 [0, 5, 4, 3, 0, 1],
 [0, 0, 4, 3, 2, 1],
 [0, 0, 0, 3, 2, 1],
 [0, 0, 0, 0, 2, 1],
 [0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0]]

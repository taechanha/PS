from itertools import product as pd
from platform import python_branch
from sys import stdin

# 1. 모듈화 - [v]
# 2. 기능 별로 설명 달기 - [partially v]

def fish_move(dx, dy, shark_r, shark_c, smell, copied_board, board):
    # global dx, dy, shark_r, shark_c, smell, copied_board, board
    # move fish
    for r in range(4):
        for c in range(4):
            for k in range(8):  # 모든 방향
                target = k
                while True:
                    nr = r + dx[target]
                    nc = c + dy[target]
                    if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark_r, shark_c) and smell[nr][nc] == 0:
                        copied_board[nr][nc][target] += board[r][c][k]
                        break
                    else:
                        #      ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
                        #dx = [0, -1, -1, -1, 0, 1, 1,  1]
                        #dy = [-1, -1, 0,  1, 1, 1, 0, -1]
                        target = (target + 7) % 8
                        # 7번 다 돌았다는 것은 움직일 수 없다는 것. break
                        if target == k:
                            copied_board[r][c][k] += board[r][c][k]
                            break

def shark_move(dx, dy, shark_r, shark_c, smell, copied_board):
    # find the best way to move shark
    best = -1
    best_move = (0, 0, 0)

    # try out moving shark (virtually)
    # 상좌하우 순으로 진행하는 이유?
    #   -> best가 여러 개인 경우, 사전 순으로 가장 빠른 것 선택해야.
    #       -> 사전 순 충족시키기 위해서
    #          -> 이렇게 하면 best를 여러 개 채워놓고, for문 돌면서 사전 순 체크해서 최종선택 하는 과정 필요 없게 됨
    #
    # 왜 pd(repeat=3)을 썼지?
    #   -> 상어가 움직일 수 있는 경우는 상상상, 상상좌, ..., 좌좌상, 좌우상, 우하하, 우상좌, 우우하, 우우우
    #       -> 즉, 중복순열: 모든 경우를 중복 포함해서 다 셈

    #               상 좌 하 우
    for case in pd([2, 0, 6, 4], repeat=3):
        curr_best = 0
        new_r, new_c = shark_r, shark_c
        visited = set()
        for move in case:
            new_r += dx[move]
            new_c += dy[move]
            if not (0 <= new_r < 4 and 0 <= new_c < 4):
                break
            if (new_r, new_c) not in visited:
                # board[r][c]에 위치한 모든 방향(0~8)의 fish의 수를 더함
                # 가장 "많이" 먹은 fish의 개수를 구하기 위해.
                curr_best += sum(copied_board[new_r][new_c])
                visited.add((new_r, new_c))
        else:
            if curr_best > best:
                best = curr_best
                best_move = case

    #      ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
    #dx = [0, -1, -1, -1, 0, 1, 1,  1]
    #dy = [-1, -1, 0,  1, 1, 1, 0, -1]
    # best move가 (2, 2, 2)면, 상상상이라는 이야기.
    # 그에 따라서 shark_r, shark_c를 옮겨준다.
    # move shark
    for move in best_move:
        shark_r += dx[move]
        shark_c += dy[move]
        for dir in range(8):
            # copied_board[x][y][z]가 0이 아니라면, 거기에 fish가 존재함.(0이 아니면 먹을 것이 없어서 smell 못 남김)
            if copied_board[shark_r][shark_c][dir] != 0:
                # 따라서, fish를 먹고,
                copied_board[shark_r][shark_c][dir] = 0
                # smell을 남긴다.
                smell[shark_r][shark_c] = 3

def fish_move(dx, dy, shark_r, shark_c, smell, copied_board, board):
    # global dx, dy, shark_r, shark_c, smell, copied_board, board
    # move fish
    for r in range(4):
        for c in range(4):
            for k in range(8):  # 모든 방향
                target = k
                while True:
                    nr = r + dx[target]
                    nc = c + dy[target]
                    if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark_r, shark_c) and smell[nr][nc] == 0:
                        copied_board[nr][nc][target] += board[r][c][k]
                        break
                    else:
                        #      ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
                        #dx = [0, -1, -1, -1, 0, 1, 1,  1]
                        #dy = [-1, -1, 0,  1, 1, 1, 0, -1]
                        target = (target + 7) % 8
                        # 7번 다 돌았다는 것은 움직일 수 없다는 것. break
                        if target == k:
                            copied_board[r][c][k] += board[r][c][k]
                            break

def copy_board():
    # make copy board for copying
    # copied_board: [r][c][dir] | dir's range is 8 which refers to the number of directions
    return [[[0 for _ in range(8)] for _ in range(4)] for __ in range(4)]

def decrease_smell(smell):
    # decrease smell
    for r in range(4):
        for c in range(4):
            if smell[r][c] > 1:
                smell[r][c] -= 1
            # smell[r][c] = max(0, smell[r][c] - 1)

def cast_copy_magic(copied_board, board):
    # finish copy magic
    for r in range(4):
        for c in range(4):
            for k in range(8):
                board[r][c][k] += copied_board[r][c][k]
    # print("after copying...")

def count_fishes(board) -> int:
    # count the number of fishes
    ans = 0
    for r in range(4):
        for c in range(4):
            ans += sum(board[r][c])
    return ans

def solve():
    #     ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
    dx = [0, -1, -1, -1, 0, 1, 1,  1]
    dy = [-1, -1, 0,  1, 1, 1, 0, -1]

    M, S = map(int, stdin.readline().split())
    smell = [[0] * 4 for _ in range(4)]
    # number of fish at board[row][col][direction]
    board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    for _ in range(M):
        x, y, d = map(int, stdin.readline().split())
        board[x - 1][y - 1][d - 1] += 1
    shark_r, shark_c = map(int, stdin.readline().split())
    shark_r, shark_c = shark_r-1, shark_c-1

    while S:
        S -= 1

        copied_board = copy_board()
        fish_move(dx, dy, shark_r, shark_c, smell, copied_board, board)
        shark_move(dx, dy, shark_r, shark_c, smell, copied_board)
        decrease_smell(smell)
        cast_copy_magic(copied_board, board)

        # debug()
        ans = count_fishes(board)

    print(ans)


solve()


# def debug(mode=0):
#     for i in range(4):
#         print(i, '|', end=' ')
#         for j in range(4):
#             print(j, ':', end='')
#             if mode == 0:
#                 for num, flag in zip(board[i][j], '←↖↑↗→↘↓↙'):
#                     print(flag * num, end='')
#             else:
#                 for num, flag in zip(copied_board[i][j], '←↖↑↗→↘↓↙'):
#                     print(flag * num, end='')
#             print(' | ', end='')
#         print()





### 모듈화 전 코드 ###
def hide_code():
    # from itertools import product as pd
    # from sys import stdin

    # #     ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
    # dx = [0, -1, -1, -1, 0, 1, 1,  1]
    # dy = [-1, -1, 0,  1, 1, 1, 0, -1]

    # M, S = map(int, stdin.readline().split())
    # smell = [[0] * 4 for _ in range(4)]
    # # number of fish at board[row][col][direction]
    # board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    # for _ in range(M):
    #     x, y, d = map(int, stdin.readline().split())
    #     board[x - 1][y - 1][d - 1] += 1
    # shark_r, shark_c = map(int, stdin.readline().split())
    # shark_r, shark_c = shark_r-1, shark_c-1

    # # def debug(mode=0):
    # #     for i in range(4):
    # #         print(i, '|', end=' ')
    # #         for j in range(4):
    # #             print(j, ':', end='')
    # #             if mode == 0:
    # #                 for num, flag in zip(board[i][j], '←↖↑↗→↘↓↙'):
    # #                     print(flag * num, end='')
    # #             else:
    # #                 for num, flag in zip(copy_board[i][j], '←↖↑↗→↘↓↙'):
    # #                     print(flag * num, end='')
    # #             print(' | ', end='')
    # #         print()

    # for _ in range(S):
    #     # make copy board for copying
    #     # copy_board: [r][c][dir] | dir's range is 8 which refers to the number of directions
    #     copy_board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]
    #     # move fish
    #     for r in range(4):
    #         for c in range(4):
    #             for k in range(8):  # 모든 방향
    #                 target = k
    #                 while True:
    #                     nr = r + dx[target]
    #                     nc = c + dy[target]
    #                     if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (shark_r, shark_c) and smell[nr][nc] == 0:
    #                         copy_board[nr][nc][target] += board[r][c][k]
    #                         break
    #                     else:
    #                         # if not available, turn 45 CCW.
    #                         #      ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
    #                         #dx = [0, -1, -1, -1, 0, 1, 1,  1]
    #                         #dy = [-1, -1, 0,  1, 1, 1, 0, -1]
    #                         target = (target + 7) % 8
    #                         # 7번 다 돌았다는 것은 움직일 수 없다는 것. break
    #                         if target == k:
    #                             copy_board[r][c][k] += board[r][c][k]
    #                             break
    #     # print("after move...")
    #     # debug(1)

    #     # find the best way to move shark
    #     best = -1
    #     best_move = (0, 0, 0)

    #     # try out moving shark (virtually)
    #     # 상좌하우 순으로 진행하는 이유?
    #     #   -> best가 여러 개인 경우, 사전 순으로 가장 빠른 것 선택해야.
    #     #       -> 사전 순 충족시키기 위해서
    #     #          -> 이렇게 하면 best를 여러 개 채워놓고, for문 돌면서 사전 순 체크해서 최종선택 하는 과정 필요 없게 됨
    #     #
    #     # 왜 pd(repeat=3)을 썼지?
    #     #   -> 상어가 움직일 수 있는 경우는 상상상, 상상좌, ..., 좌좌상, 좌우상, 우하하, 우상좌, 우우하, 우우우
    #     #       -> 즉, 중복순열: 모든 경우를 중복 포함해서 다 셈

    #     #               상 좌 하 우
    #     for case in pd([2, 0, 6, 4], repeat=3):
    #         curr_best = 0
    #         new_r, new_c = shark_r, shark_c
    #         visited = set()
    #         for move in case:
    #             new_r += dx[move]
    #             new_c += dy[move]
    #             if not (0 <= new_r < 4 and 0 <= new_c < 4):
    #                 break
    #             if (new_r, new_c) not in visited:
    #                 # board[r][c]에 위치한 모든 방향(0~8)의 fish의 수를 더함
    #                 # 가장 "많이" 먹은 fish의 개수를 구하기 위해.
    #                 curr_best += sum(copy_board[new_r][new_c])
    #                 visited.add((new_r, new_c))
    #         else:
    #             if curr_best > best:
    #                 best = curr_best
    #                 best_move = case

    #     print("best move: ", best_move)
    #     #      ←, ↖,  ↑,  ↗,  →, ↘, ↓,  ↙
    #     #dx = [0, -1, -1, -1, 0, 1, 1,  1]
    #     #dy = [-1, -1, 0,  1, 1, 1, 0, -1]
    #     # best move가 (2, 2, 2)면, 상상상이라는 이야기.
    #     # 그에 따라서 shark_r, shark_c를 옮겨준다.
    #     # move shark
    #     for move in best_move:
    #         shark_r += dx[move]
    #         shark_c += dy[move]
    #         for dir in range(8):
    #             # copy_board[x][y][z]가 0이 아니라면, 거기에 fish가 존재함.(0이 아니면 먹을 것이 없어서 smell 못 남김)
    #             if copy_board[shark_r][shark_c][dir] != 0:
    #                 # 따라서, fish를 먹고,
    #                 copy_board[shark_r][shark_c][dir] = 0
    #                 # smell을 남긴다.
    #                 smell[shark_r][shark_c] = 3
                    

    #     # decrease smell
    #     for r in range(4):
    #         for c in range(4):
    #             if smell[r][c] > 1:
    #                 smell[r][c] -= 1
    #             # smell[r][c] = max(0, smell[r][c] - 1)

    #     # finrsh copy magic
    #     for r in range(4):
    #         for c in range(4):
    #             for k in range(8):
    #                 board[r][c][k] += copy_board[r][c][k]
    #     # print("after copying...")
    #     # debug()

    # # count the number of fishes
    # ans = 0
    # for i in range(4):
    #     for c in range(4):
    #         ans += sum(board[r][c])

    # print(ans)

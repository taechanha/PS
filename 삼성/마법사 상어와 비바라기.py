# 모르는 것
# 1.어떻게 끝과 끝을 연결하지? [v]

# 2시간 소요

class Cloud:
    def __init__(self, r, c) -> None:
        self.r = r
        self.c = c

    def move(self, dir, dist):
        for _ in range(dist):
            nr = self.r + dr[dir]
            nc = self.c + dc[dir]
            if nr < 0:
                nr = n - 1
            if nc < 0:
                nc = n - 1
            if nr > n - 1:
                nr = 0
            if nc > n - 1:
                nc = 0
            self.r = nr
            self.c = nc


def out_of_bound(r, c) -> bool:
    return not (0 <= r < n and 0 <= c < n)


def possible_diag_pos(board, r, c) -> list:
    # (r, c): current poisiton to get diagonal items from
    ret = []
    for i in [2, 4, 6, 8]:
        nr = r + dr[i]
        nc = c + dc[i]
        if out_of_bound(nr, nc):
            continue
        if board[nr][nc] == 0:
            continue
        ret.append((nr, nc))
    return ret


def more_than_2_pos(board) -> list:
    ret = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 2:
                ret.append((i, j))
    return ret


def count_water(board) -> int:
    return sum([sum(row) for row in board])


global n, m, board, ds
n, m = map(int, input().split())
board, ds = [], []
for _ in range(n):
    board.append(list(map(int, input().split())))
for _ in range(m):
    dir, dist = map(int, input().split())
    ds.append((dir, dist))
# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
# 초기 구름 (N, 1), (N, 2), (N-1, 1), (N-1, 2)
cloud_list: list[Cloud] = []
for r, c in [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]:
    cloud_list.append(Cloud(r, c))


# 절차
# 1. 구름 이동 (di 방향, si 거리)
for dir, dist in ds:
    just_rained_list = []
    cloud_gone_list = []
    temp_board = [row[:] for row in board]
    # 구름 이동
    for cloud in cloud_list:
        cloud.move(dir, dist)  # 호출 후 각 cloud 위치 변화

    # # DEBUG: 보드 상태
    # print(temp_board)
    # exit()

    # DEBUG - 이동
    # print()
    # for cloud in cloud_list:
    #     print(cloud.r, cloud.c)
    # print()
    # exit()
    # END DEBUG

    # 2. 구름에서 비 내림 (구름 밑 바구니 물의 양 1 증가)
    for cloud in cloud_list:
        # * 비 내리는 과정 중에 서로 겹치는 경우 방지 위해 새 보드에 할당
        temp_board[cloud.r][cloud.c] = board[cloud.r][cloud.c] + 1
        # 비 내린 곳 저장
        just_rained_list.append((cloud.r, cloud.c))
        # 미리 사라진 구름 저장
        cloud_gone_list.append((cloud.r, cloud.c))

    # 업데이트
    board = [row[:] for row in temp_board]

    # # DEBUG: 보드 상태
    # print(temp_board)
    # exit()

    # 3. 구름 사라짐
    cloud_list: list[Cloud] = []
    # 4. [2.]에서 물이 증가한 칸(r, c)에 물복사버그:
    #    - '대각선 방향 거리 1인 칸에 물이 있는 바구니의 수'만큼 (r, c) + 1
    #    - 경계를 넘어가는 칸은 대각선 방향 거리 1아님
    for r, c in just_rained_list:
        diag_bucket_num = len(possible_diag_pos(board, r, c))
        # *
        temp_board[r][c] = board[r][c] + diag_bucket_num

    # for r, c in just_rained_list:
        # print((r,c), possible_diag_pos(r, c))
    # exit()

    # DEBUG: 보드 상태 - [x]
    # print(temp_board)
    # exit()

    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에
    #    - 구름 생기고
    #    - '물의 양 - 2',
    #    - [3.]에서 구름 사라진 칸은 제외
    more_than_2_list = more_than_2_pos(temp_board)
    # 3.에서 구름 사라진 칸 제외
    for r, c in cloud_gone_list:
        if (r, c) in more_than_2_list:
            more_than_2_list.remove((r, c))
    # 각 위치에 구름 생성, 물의 양 - 2
    for r, c in more_than_2_list:
        cloud_list.append(Cloud(r, c))
        temp_board[r][c] -= 2

    # DEBUG - 생성
    # print()
    # for cloud in cloud_list:
    #     print(cloud.r, cloud.c)
    # print()
    # exit()
    # END DEBUG

    # 업데이트
    board = [row[:] for row in temp_board]

# M번의 이동 후 물의 양의 합
print(count_water(board))

# 5 4
# 0 0 1 0 2
# 2 3 2 1 0
# 4 3 2 9 0
# 1 0 2 9 0
# 8 8 2 1 0
# 1 3
# 3 4
# 8 1
# 4 8


# (r, c)

# 1. (0, c)
#   1-1. 위로   : (n-1, c)
#   1-2. 왼쪽으로:

# 2. (n-1, c)에서 아래로 -> (0, c)
# 3. (r, 0)에서 왼쪽으로 -> (r, n-1)
# 3. (r, n-1)에서 오른쪽으로 -> (r, 0)

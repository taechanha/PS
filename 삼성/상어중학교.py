
from threading import local


class Group:
    def __init__(self, block_list, base_block) -> None:
        self.block_list: list = block_list
        self.base_block: tuple = base_block

    def count_rainbow_blocks(self, board):
        # 0: rainbow
        cnt = 0
        for block in self.block_list:
            r, c = block
            # print("b: ", block)
            if board[r][c] == 0:
                cnt += 1
        return cnt


def out_of_bound(r, c):
    return not (0 <= r < n and 0 <= c < n)


def dfs(r, c, visited) -> list:
    stack = [(r, c)]
    # visited.append((r, c))
    local_visited = [(r, c)]
    base_color = board[r][c]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if out_of_bound(nr, nc):
                continue
            if (nr, nc) in visited:
                continue
            if (nr, nc) in local_visited:
                continue
            if board[nr][nc] == -1:
                continue
            if (board[nr][nc] == base_color) or (board[nr][nc] == 0):
                stack.append((nr, nc))
                local_visited.append((nr, nc))

    return local_visited


def get_rainbox_cnt_max(board, group_list):
    rainbow_cnt_max = -1
    for group in group_list:
        rainbow_cnt_max = max(
            rainbow_cnt_max, group.count_rainbow_blocks(board))
    return rainbow_cnt_max


def find_group_with_max_rainbow(board, group_list: list[Group]) -> list:
    rainbow_cnt_max = get_rainbox_cnt_max(board, group_list)

    ret = []
    for i, group in enumerate(group_list):
        if rainbow_cnt_max == group.count_rainbow_blocks(board):
            # print(group)
            ret.append(group)
    return ret


def sort_list(block_list):
    return sorted(block_list, key=lambda x: (-x.base_block[0], -x.base_block[1]))


def print_group(group):
    for group in group_list:
        print("each group: ", group.block_list)


def remove_block(board, group: Group) -> int:
    # group: [(r1, c1), (r2, c2), ...]
    for r, c in group.block_list:
        board[r][c] = -2
    return len(group.block_list)**2


def gravitate(board) -> list[list]:
    # 보드 밑에서부터 위로 올라가면서 -1, -2를 제외한 애들 밑으로 내리기
    temp_board = [row[:] for row in board]
    n = len(board)
    m = len(board[0])
    for c in range(n):
        for r in range(m-1, -1, -1):
            # print(r, c)
            if temp_board[r][c] == -2:
                # 현재는 참
                temp_r = r
                fl = 0
                while temp_board[temp_r][c] == -2:
                    if temp_r == 0:
                        fl = 1
                        break
                    temp_r -= 1
                if temp_board[temp_r][c] == -1:
                    continue
                # board[temp_r][c] == '#' and temp_r == 0
                if fl == 1:
                    # do nothing
                    pass
                # board[temp_r][c] != '#'
                else:
                    temp_board[r][c] = temp_board[temp_r][c]
                    temp_board[temp_r][c] = -2
    return temp_board


def rotate_ccw_90(board) -> list[list]:
    n = len(board)
    m = len(board[0])
    ret = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(m):
            ret[n-1-c][r] = board[r][c]
    return ret


# def init_rainbow(board, visited):
#     ret = []
#     print(visited)
#     exit()
#     for r, c in visited:
#         if board[r][c] == 0:
#             continue
#         ret.append((r, c))
#     return ret
# 1. 가장 큰 그룹 찾기 - dfs
#   - 일반 블록이 적어도 하나
#   - 일반 블록의 색은 모두 같아야
#   - 검은색 블록 포함 안 됨
#   - 무지개 블록은 상관 없음
#   - 블록의 개수는 2 이상
#   - 한 블록이 그룹 내부에서 인접한 칸을 통해 그룹 내부 모든 곳으로 이동 가능해야
#   - *** 기준 블록: 무지개 블록이 아닌 블록 중 행의 번호가 가장 작은 블록, 여러 개면 열의 번호가 가장 작은 블록

# 2. 오토 플레이
#   1) 블록 그룹이 존재하는 동안 계속 반복 """ while check """ [v]
#   2) 크기가 가장 큰 블록 그룹 찾기: """ dfs """ [v]
#   3) 여러 개라면, 그 중 무지개 블록 수가 가장 많은 그룹 """ count_rainbow """ [v]
#   1) 여러 개라면, 기준 블록의 행이 가장 큰 것 """ sort 후 첫 번째 """ [v]
#   1) 여러 개라면, 기준 블록의 열이 가장 큰 것 """ 위와 같은 결과로 결정됨 """ [v]
#   1) 여기서 찾은 블록 그룹의 모든 블록 제거, (블록 수)^2 만큼 점수 획득 """ remove_block """ []
#   1) 중력 작용: 검은색 블록을 제외한 모든 블록 밑으로 (다른 블록 만나거나 벽 만나기 까지) """ gravitate """ []
#   1) 반 시계 방향 90도 회전 """ rotateccw90 """ []
#   1) 중력 작용 """ gravitate """ []


# 3. 오토플레이가 전부 끝났을 때 점수의 합

# 1. 가장 큰 그룹 찾기 - dfs
#   - 일반 블록이 적어도 하나     [v]
#   - 일반 블록의 색은 모두 같아야 [v]
#   - 검은색 블록 포함 안 됨     [v]
#   - 무지개 블록은 상관 없음     [v]
#   - 블록의 개수는 2 이상       [v]
#   - 한 블록이 그룹 내부에서 인접한 칸을 통해 그룹 내부 모든 곳으로 이동 가능해야
#   - *** 기준 블록: 무지개 블록이 아닌 블록 중 행의 번호가 가장 작은 블록, 여러 개면 열의 번호가 가장 작은 블록
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

ans = 0
i = 0
while 1:
    # 플레이마다 리셋
    i += 1
    visited = []
    group_list: list[Group] = []
    block_list = []

    for r in range(n):
        for c in range(n):
            if board[r][c] == -1 or board[r][c] == 0 or board[r][c] == -2:
                continue
            if (r, c) in visited:
                continue
            # print((r, c))
            block_list = dfs(r, c, visited)
            if len(block_list) == 0:
                continue

            for x, y in block_list:
                if board[x][y] != 0:
                    visited.append((x, y))
            # visited += block_list[:]  # [(a,b), (c, d)] = [(e, f)]
            # if block_list == [(1, 0), (2, 0), (1, 1), (2, 1), (3, 1), (2, 2), (4, 1), (4, 0)]:
                # print(visited, (r, c))

            # base_block = (r, c)
            block_list.sort(key=lambda x: (x[0], x[1]))
            for r, c in block_list:
                if board[r][c] != 0:
                    base_block = (r, c)
                    break

            if len(block_list) < 2:
                continue
            group_list.append(Group(block_list[:], base_block))

    # rainbow 제일 많은 놈 고르기
    group_list = find_group_with_max_rainbow(board, group_list)
    group_list = sort_list(group_list)

    # termination condition
    if not group_list:
        print(ans)
        exit()

    # group rather than group_list
    group = group_list[0]
    group_list = []

    # 블록 제거
    ans += remove_block(board, group)
    # 중력
    board = gravitate(board)
    # rotate ccw 90
    board = rotate_ccw_90(board)
    # 중력
    board = gravitate(board)


print("answer: ", ans)

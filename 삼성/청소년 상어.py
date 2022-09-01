# 4x4 공간

# 흐름
# - 상어 0,0에서 물고기 먹음
# - 물고기 이동
# - 상어 이동
# - 물고기 이동
# - ... 상어 이동 불가까지
# - 이걸 모든 경우에 대해 탐색해서 그 중 상어가 먹은 물고기 최대값

# 상어
# - 위치
# - 방향
# - 이동
#     - 방향에 있는 칸으로 한 번에 여러 개의 칸 이동 가능
#     - 물고기 먹으면 그 물고기의 방향 획득
#     - 이동하는 중의 물고기는 먹지 않음
#     - 물고기가 없는 칸으로는 이동 불가 - 방향에 있는 칸 탐색 후 물고기가 하나도 없으면 이동하지 않는다는 말인듯
# - 처음에 0,0 물고기 먹고 시작


# 물고기
# - 위치
# - 방향
# - 이동
#     - 번호 작은 것 부터
#     - 이동 시 물고기의 방향 획득
#     - 이동 가능한 칸: 빈 칸 혹은 다른 물고기가 있는 칸
#     - 이동 불가능한 칸: 상어 혹은 경계 넘는 칸
#         - 이동할 수 있을 때까지 반시계 45도 회전 -> 그래도 이동 불가하면 이동하지 않음
#     - 이동 시 그 물고기와 서로 스왑(방향까지): 빈 칸이면 스왑 x

class Fish:
    def __init__(self, r, c, idx, dir) -> None:
        self.r = r
        self.c = c
        self.idx = idx
        self.dir = dir


def play(r, c, dir, cnt):
    global max_cnt
    if should_terminate(r, c, dir):
        max_cnt = max(max_cnt, cnt)
        return
    else:
        # - 물고기 이미 먹은 상태 -
        fishes_move(0, 0)
        # 갈 수 있는 칸 리스트
        reachable_cells = get_reachable_cells(r, c, dir)
        for nr, nc, ndir in reachable_cells:
            # 상어 이동, 물고기 먹기
            cnt += board[nr][nc].idx
            fish = board[nr][nc]
            board[nr][nc] = None
            play(nr, nc, ndir, cnt)
            board[nr][nc] = fish
            cnt -= board[nr][nc].idx


def should_terminate(r, c, dir):
    return len(get_reachable_cells(r, c, dir)) == 0


def out_of_bound(r, c):
    return not (0 <= r < 4 and 0 <= c < 4)


def get_reachable_cells(r, c, dir):
    # 상어의 현재 위치와 방향에서 갈 수 있는 칸 리스트 반환
    reachable_cells = []
    for _ in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if out_of_bound(nr, nc):
            continue
        if board[nr][nc] == None:
            continue
        reachable_cells.append((nr, nc, board[nr][nc].dir))
        r = nr
        c = nc
    return reachable_cells


def fishes_move(shark_r, shark_c):
    fish_list = []
    for i in range(4):
        for j in range(4):
            fish = board[i][j]
            if fish:
                fish_list.append(fish)

    fish_list.sort(key=lambda fish: fish.idx)

    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
    # 이동 가능할 때까지 반시계 방향 45 회전
    rotate = {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 0
    }
    for fish in fish_list:
        for i in range(9):
            if i == 0:
                nr = fish.r + dr[fish.dir]
                nc = fish.c + dc[fish.dir]

            nr = fish.r + dr[rotate[fish.dir]]
            nc = fish.c + dc[rotate[fish.dir]]

            fish.dir = rotate[fish.dir]

            if out_of_bound(nr, nc):
                continue
            # 상어 존재
            if (nr, nc) == (shark_r, shark_c):
                continue
            # 빈 칸
            if board[nr][nc] == None:
                board[nr][nc] = Fish(nr, nc, fish.idx, fish.dir)
                board[fish.r][fish.c] = None
                break
            # 물고기 존재
            else:
                # 물고기 스왑
                for each_fish in fish_list:
                    if (each_fish.r, each_fish.c) == (nr, nc):
                        each_fish.r, each_fish.c = fish.r, fish.c
                        break
                # 위치 바꿈
                board[nr][nc], board[fish.r][fish.c] = \
                    Fish(nr, nc, fish.idx, fish.dir), \
                    Fish(fish.r, fish.c, board[nr][nc].idx, board[nr][nc].dir)
                break


board = [[None] * 4 for _ in range(4)]
for k in range(4):
    input_list = list(map(int, input().split()))
    for i in range(4):
        # 01 23 45 67
        idx = input_list[(i*2)] - 1
        dir = input_list[(i*2)+1] - 1
        board[k][i] = Fish(k-1, i-1, idx, dir)

#      ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
max_cnt = 0

max_cnt += board[0][0].idx
dir = board[0][0].dir
board[0][0] = None
play(0, 0, dir, max_cnt)

print(max_cnt)

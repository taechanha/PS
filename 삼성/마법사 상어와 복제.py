# 1. 복제 마법 (5에 발효)
# 2. 모든 물고기 이동
#   - 만약 상어, 냄새, 격자 범위인 경우,
#       - 방향 45도 회전
#          - 이동할 수 있는 칸이 없으면 이동 X
# 3. 상어 연속 3칸 이동
#     - 상하좌우 인접 칸, 격자 범위 - 물고기 있으면 물고기 먹음
#        - 물고기가 먹힌 경우, 냄새 남김
#     * 가능한 이동 방법 중 가장 물고기가 많은 쪽으로 (현재 상태에서 말하는 거 겠지?)
#        - 많은 경우가 여러가지라면, 사전 순으로 가장 앞서는 방법.
#            - 사전 순으로 변환
#               - 상:1, 좌:2, 하:3, 우:4   ->  이어 붙이기 Ex. 132 < 333  ->  [132 선택]
# 4. 물고기 냄새 사라짐 (정리하면, 물고기 이동 -> 상어 이동 -> 냄새 사라짐)
# 5. 복제 마법 시전. (1에서의 위치 복제)
def is_in_boundary(i, j):
    return 0 <= i < 4 and 0 <= j < 4


def count_fishes() -> int:
    cnt = 0
    for r in range(4):
        for c in range(4):
            cnt += len(fish_board[r][c])
    return cnt


def replicate_fishes():
    pass


def fish_rotate_and_move():
    for r in range(4):
        for c in range(4):
            fish_count = fish_board[r][c]
            print(fish_count)
            for k in range(len(fish_count)):
                fish_move(r, c, k)


def fish_move(r, c, fish_idx):
    curr_dir = fish_board[r][c][fish_idx] - 1
    #     ←,  ↖,  ↑,  ↗, →, ↘, ↓, ↙
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0,  1, 1, 1, 0, -1]
    for dir in range(0, -8, -1):
        nr = r + dr[curr_dir + dir]
        nc = c + dc[curr_dir + dir]
        if not is_in_boundary(nr, nc):
            continue
        if smell_board[nr][nc] == True:
            continue
        if shark_board[nr][nc] == 's':
            continue
        if curr_dir + dir >= 0:
            dir = curr_dir + dir + 1
        else:
            dir = curr_dir + dir + 9

        try:
            fish_board[r][c][fish_idx] = dir
        except:
            # print(fish_board[r][c], fish_idx)
            return

        fish = fish_board[r][c].pop(fish_idx)
        fish_board[nr][nc].append(fish)

# problem: 2차원 배열 각 칸에 여러 요소 한 번에 담기

# 어떻게 풀 수 있을까?
# -> 3차원 배열을 만든다.
#    -> (2차원 배열 요소에 [] 리스트를 삽입하여 something[r][c] 안에 요소 삽입 가능케 한다.)


""" 초기 상어 위치에 물고기 있는 경우도 처리해야함 """


def shark_move():
    def dfs(r, c, cnt, chosen):
        if not is_in_boundary(r, c):
            return
        if cnt == 0:
            positions.append(chosen)

        chosen.append((r+1, c))
        dfs(r+1, c, cnt-1, chosen)
        chosen.pop()

        chosen.append((r-1, c))
        dfs(r-1, c, cnt-1, chosen)
        chosen.pop()

        chosen.append((r, c+1))
        dfs(r, c+1, cnt-1, chosen)
        chosen.pop()

        chosen.append((r, c-1))
        dfs(r, c-1, cnt-1, chosen)
        chosen.pop()

    positions = []
    chosen = []
    dfs(0, 0, 3, chosen)
    # print(positions)

    # [ [ (a, b), (c, d), (d, e) ], [ (f, g), ... ] ]
    print("pos: ", positions)
    eaten_fishes_count = []
    for position in positions:
        cnt = 0
        for r, c in position:
            cnt += len(fish_board[r][c])
        eaten_fishes_count.append(cnt)
    print(eaten_fishes_count)

#    - 연속 3칸 이동(상상상, 상하좌, 모든 케이스 가능. 64가지.)
#       - 칸 이동 중 만나는 물고기는 모두 제거
#           - 냄새 남김
#       - 이동 중 범위 벗어나는 경로는 불가
#       - 가능한 가장 많은 물고기를 먹는 쪽으로(위치 저장해두고, 가장 많은 놈 고른다음, 삭제 처리)
    pass


def leave_smell():
    pass


def smell_disappear():
    pass


def solve():
    smell_disappear_counter = 0
    practice_cnt = s
    while practice_cnt:
        practice_cnt -= 1
        fish_rotate_and_move()
        shark_move()
        if smell_disappear_counter != 0 and smell_disappear_counter % 2 == 0:
            smell_disappear()
        replicate_fishes()
        smell_disappear_counter += 1

    num_fishes = count_fishes()
    return num_fishes

# action:
#   - 복제: 그냥 초깃값 물고기 개수를 5에서 더 해주면 되는거 아닌가?
#   - 물고기:
#       - 방향 회전(반시계 45도): Ex. 8->7, 7->6, ..., 1->8
#       - 이동할 수 있을 때까지 회전하는 것임. 한 번에
#       - 회전 한 다음 이동도 함 (하나의 동작)
#   - 상어:
#       - 연속 3칸 이동(상상상, 상하좌, 모든 케이스 가능. 64가지.)
#       - 칸 이동 중 만나는 물고기는 모두 제거
#           - 냄새 남김
#       - 이동 중 범위 벗어나는 경로는 불가
#       - 가능한 가장 많은 물고기를 먹는 쪽으로(위치 저장해두고, 가장 많은 놈 고른다음, 삭제 처리)
#   - 냄새:
#       - 연습 2번 지나야 사라짐. 1에서 생겼으면 3에서 사라짐 (3에서 물고기 이동, 상어 이동 후)

# subject's condition:
#   - 물고기: 상어, 냄새, 격자 범위인 경우 "회전"
#


# conditions:
# board: 4 x 4
#    ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# d = [1, 2, 3, 4, 5, 6, 7, 8]

# global b, m, s, fishes, shark, fish_board, shark_board, smell_board
m, s = map(int, input().split())
fish_board = [[[] for __ in range(4)] for _ in range(4)]
for _ in range(m):
    a, b, c = map(int, input().split())
    fish_board[a-1][b-1].append(c)

r, c = map(int, input().split())
shark_board = [[0] * 4 for _ in range(4)]
shark_board[r-1][c-1] = 's'
smell_board = [[False] * 4 for _ in range(4)]

solve()


# 5 1
# 4 3 5
# 1 3 5
# 2 4 2
# 2 1 6
# 3 4 4
# 4 2

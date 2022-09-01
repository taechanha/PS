

def out_of_bound(r, c):
    return not(0 <= r < 4 and 0 <= c < 4)


def play(shark_r, shark_c, shark_d, cur_cnt):
    global max_cnt, board, rotate
    temp_board = [row[:] for row in board]
    # eat
    # 현재 위치의 물고기 먹기
    # - 물고기의 인덱스 만큼을 cur_cnt += [v]
    # - 물고기의 방향을 상어의 방향에 할당 [v]
    # - 물고기 삭제 [v]
    # - 물고기 되돌리기 []
    cur_cnt += board[shark_r][shark_c].idx
    if cur_cnt > max_cnt:
        max_cnt = cur_cnt
    shark_d = board[shark_r][shark_c].dir
    board[shark_r][shark_c] = None

    # fish move
    # 순서가 작은 물고기부터 움직인다. - 순서에 따라 리스트에 담는다. [v]
    # - for 문을 통해 0번 물고기부터 돈다. 물고기가 죽어 있는 경우는 pass [v]
    # - 현재 위치와 방향을 바탕으로, 이동할 수 있는 칸을 확인한다. (빈 칸, 다른 물고기 <-> 상어, 경계) [v]
    # - 이동할 수 있는 칸을 발견할 때까지 반시계로 45도 회전한다(8번) [v]
    # - 그래도 이동할 수 없으면 가만히 있는다. [v]
    # - 다른 물고기가 있는 칸으로 이동할 때는 '''위치만''' 바꾼다. [v]
    fishes = [None] * 16
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                FISH = board[i][j]
                # print(FISH.idx)
                fishes[FISH.idx] = FISH

    print(fishes)
    for i in range(len(fishes)):
        if fishes[i] == None:
            continue
        FISH = fishes[i]
        for j in range(9):
            if j == 0:
                nr = FISH.r + dr[FISH.dir]
                nc = FISH.c + dc[FISH.dir]
            else:
                nr = FISH.r + dr[rotate[FISH.dir]]
                nc = FISH.c + dc[rotate[FISH.dir]]
                FISH.dir = rotate[FISH.dir]

            if out_of_bound(nr, nc):
                continue
            if (nr, nc) == (shark_r, shark_c):
                continue
            # empty cell
            if board[nr][nc] == None:
                board[FISH.r][FISH.c] = None
                board[nr][nc] = FISH
                FISH.r = nr
                FISH.c = nc
                fishes[i] = Fish(FISH.idx, FISH.r, FISH.c, FISH.dir)
                break
            # there exists an another fish
            else:
                if board[FISH.r][FISH.c] == None:
                    print("ZXCZXCASDADQWQW", FISH.r, FISH.c)
                board[FISH.r][FISH.c], board[nr][nc] = board[nr][nc], board[FISH.r][FISH.c]
                board[FISH.r][FISH.c].r, board[FISH.r][FISH.c].c = nr, nc
                board[nr][nc].r, board[nr][nc].c = FISH.r, FISH.c
                fishes[i] = Fish(FISH.idx, FISH.r, FISH.c, FISH.dir)
                NEXT_FISH = board[nr][nc]
                fishes[NEXT_FISH.idx] = Fish(
                    NEXT_FISH.idx, NEXT_FISH.r, NEXT_FISH.c, NEXT_FISH.dir)
                break

    # shark move
    # - 현재 방향과 위치를 바탕으로 움직일 수 있는 칸을 탐색한다.
    # - 움직인다.
    for i in range(1, 4):
        nr = shark_r + dr[shark_d]
        nc = shark_c + dc[shark_d]
        if out_of_bound(nr, nc):
            continue
        play(nr, nc, shark_d, cur_cnt)

    board = [row[:] for row in temp_board]


class Fish:
    def __init__(self, idx, r, c, dir) -> None:
        self.idx = idx
        self.r = r
        self.c = c
        self.dir = dir

    def __str__(self):
        return "(" + str(self.idx) + "," + str(self.r) + "," + str(self.c) + "," + str(self.dir) + ")"


board = [[None] * 4 for _ in range(4)]
for k in range(4):
    input_list = list(map(int, input().split()))
    for i in range(4):
        # 01 23 45 67
        idx = input_list[(i*2)] - 1
        dir = input_list[(i*2)+1] - 1
        board[k][i] = Fish(idx, k, i, dir)

#         ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dr = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 0, -1, -1, -1, 0, 1, 1, 1]
max_cnt = 0
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
for row in board:
    for c in row:
        print(c, end=" ")
    print()

play(0, 0, 0, 0)

print(max_cnt)

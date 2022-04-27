R, C, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
dr2 = [0, 1, 0, -1]
dc2 = [1, 0, -1, 0]

ap_pos, p = [None, None], 0
for i in range(R):
    for j in range(C):
        if board[i][j] == -1:
            ap_pos[p] = (i, j)
            p += 1

# 1. 미세먼지 확산
#   1-1. 인접한 네 방향(경계, 공기청정기 x)
#   1-2. 인접한 칸 += A_rc // 5
#   1-3. A_rc -= (A_rc // 5 x 확산 방향 수)
def spread_dust():
    global R, C
    temp_board = [[0] * C for _ in range(R)]
    temp_board[ap_pos[0][0]][ap_pos[0][1]] = -1
    temp_board[ap_pos[1][0]][ap_pos[1][1]] = -1

    for r in range(R):
        for c in range(C):
            if board[r][c] == -1 or board[r][c] == 0:
                continue
            cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if board[nr][nc] == -1:
                    continue
                temp_board[nr][nc] += board[r][c] // 5
                cnt += 1
            #
            temp_board[r][c] += board[r][c] - ((board[r][c] // 5) * cnt)
    return [row[:] for row in temp_board]

# 2. 공기청정기 작동
#   2-1. 위칸: 반시계, 아래칸: 시계 - 한 칸씩
#   2-2. 공기청정기로 들어간 먼지는 정화
def make_zero(r, c, dir, dr, dc):
    global board, temp_board, R, C
    if board[r][c] == -1:
        return
    temp_board[r][c] = 0
    for i in range(dir, 4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < R and 0 <= nc < C):
            return make_zero(nr, nc, i, dr, dc)


def move_dust(r, c, dir, prev, is_start, dr, dc):
    global board, temp_board, R, C
    if board[r][c] == -1:
        return
    if is_start == False:
        temp_board[r][c] = prev
    for i in range(dir, 4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < R and 0 <= nc < C):
            return move_dust(nr, nc, i, board[r][c], False, dr, dc)


def purify_air():
    global ap_pos, temp_board, dr, dc
    temp_board = [row[:] for row in board]
    # up
    r, c = ap_pos[0][0], ap_pos[0][1]
    # make zeros
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        make_zero(nr, nc, 0, dr, dc)
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        move_dust(nr, nc, 0, -1, True, dr, dc)
        break

    # down
    r, c = ap_pos[1][0], ap_pos[1][1]
    # make zeros
    for i in range(4):
        nr = r + dr2[i]
        nc = c + dc2[i]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        make_zero(nr, nc, 0, dr2, dc2)
        break

    for i in range(4):
        nr = r + dr2[i]
        nc = c + dc2[i]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        move_dust(nr, nc, 0, -1, True, dr2, dc2)
        break

    return [row[:] for row in temp_board]

# 3. 출력: T초 후 미세먼지의 양
def count_dust(board):
    return sum(map(sum, board)) + 2


while t:
    t -= 1

    board = spread_dust()

    board = purify_air()

    cnt = count_dust(board)

print(cnt)

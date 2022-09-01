# 9:36

# * 1번 말부터 차례대로 이동

# 1. 이동 시
#     - 각 말의 방향대로 이동
#     - 만약 말 위에 다른 말이 있다면 그 말들도 함께 이동
#     - 이동하려는 칸
#         - 흰색: 그냥 이동
#         - 빨간색: 뒤집어서 이동
#         - 파란색 or 경계: 이동 방향을 반대로 하고 이동, 그래도 파란색 or 경계이면 이동하지 않음

# 2. 이동 중 4개의 말이 겹치는 경우가 생기면 바로 종료

# 3. 출력: 게임이 종료되는 턴의 번호 (턴 수가 1000보다 크면 -1)


n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
pieces = [list(map(int, input().split())) for _ in range(k)]
board = [[None] * n for _ in range(n)]
turn_backs = {0: 1, 1: 0, 2: 3, 3: 2}
turns = 0
# →, ←, ↑, ↓
dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]
# [[2, 1, 1], [3, 2, 3], [2, 2, 1], [4, 1, 2]]
for i in range(n):
    for j in range(n):
        board[i][j] = []
for i, (r, c, d) in enumerate(pieces):
    board[r-1][c-1].append((i+1, d-1))


def out_of_bound(r, c):
    return not (0 <= nr < n and 0 <= nc < n)


def find_piece(idx):
    global board
    for i in range(n):
        for j in range(n):
            len_piggy = len(board[i][j])
            for m in range(len_piggy):
                if board[i][j][m][0] == idx:
                    return board[i][j], i, j, m
    return -1


def should_terminate(piggy):
    if len(piggy) >= 4:
        return True
    return False


def pprint(board):
    for row in board:
        print(row)


while True:
    turns += 1
    if turns > 1000:
        break
    # 가장 작은 번호의 말 부터
    for idx in range(1, k+1):
        try:
            piggy, r, c, m = find_piece(idx)
        except:
            print(turns, find_piece(idx), idx)
            for row in board:
                print(row)
            exit()

        i, dir = piggy[m][0], piggy[m][1]

        # 이동
        nr = r + dr[dir]
        nc = c + dc[dir]
        # 만약 이동하려는 칸이 파란색이거나 경계를 넘어간다면 방향 바꾼 후 다시 이동 시도
        if out_of_bound(nr, nc) or info[nr][nc] == 2:
            new_dir = turn_backs[dir]
            board[r][c][m] = (board[r][c][m][0], new_dir)
            nr = r + dr[new_dir]
            nc = c + dc[new_dir]
            # 방향을 바꿨어도 경계를 넘어가거나 파란색 칸이라면 해당 말은 움직이지 않음
            if out_of_bound(r, c) or info[nr][nc] == 2:
                continue
            # 이 경우 다음 칸이 빨간색 or 흰색이라는 의미이니, fall-through 해줌
            else:
                dir = new_dir
                pass

        # 빨간색
        if info[nr][nc] == 1:
            # 업혀진 넘들이랑 같이 뒤집어서 움직여준다..
            board[r][c][m] = (board[r][c][m][0], dir)
            reverse_piggy = list(reversed(board[r][c][m:]))
            board[nr][nc] += reverse_piggy
            # 종료조건
            if should_terminate(board[nr][nc]):
                # print("red, ", turns, pprint(board))
                print(turns)
                exit()
            # 움직였으니까 삭제해주기
            for _ in range(m, len(piggy)):
                board[r][c].pop()
            continue

        # 흰색
        if info[nr][nc] == 0:
            board[r][c][m] = (board[r][c][m][0], dir)
            board[nr][nc] += board[r][c][m:]
            # 종료조건
            if should_terminate(board[nr][nc]):
                # print("white, ", turns, pprint(board))
                print(turns)
                exit()
            for _ in range(m, len(piggy)):
                board[r][c].pop()

        # 경계 or 파란색 칸 케이스에 new_dir로 바뀌었을 수 있고,
        # 그 바뀐 넘은 m 번째 말밖에 없음. 걔의 방향을 바뀌었으니 적용

        # pprint(board)
        # print()

# if turns > 1000:
#     print(-1)
# else:
#     print(turns)

print(-1) if turns > 1000 else print(turns)

# pprint(board)

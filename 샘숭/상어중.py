# 인접: 상하좌우
# NxN
# 검은색: -1, 무지개: 0, 일반 블록: 1 <= c <= M
# 기준 블록: 무지개 블록이 아닌 블록 중 행의 번호, 열의 변호가 가장 작은 블록

# 1. 크기가 가장 큰 블록 그룹 찾기
# 개수 > 1, 일반 블록이 적어도 하나 이상,
# 일반 블록의 색은 모두 같음, 검은색 포함 x,
# 무지개 얼마든 ok, 모두 인접
# 여러 개라면, 무지개 수, 기준 블록의 행, 기준 블록의 열
# 2. 1에서 찾은 블록 그룹의 모든 블록 제거 -> 9
# 블록의 수^2 점 획득
# 3. 중력 작용
# 검은색 제외 모두 아래로
# 다른 블록을 만나거나 벽을 만날 때까지
# 4. 90도 반시계 회전
# 5. 중력 작용
def pnt():
    global board
    for row in board:
        print(row)
    print()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
EMPTY = 9
cnt = 0


def dfs(r, c, visited):
    global N, board
    stack = [(r, c)]
    visited[r][c] = True
    base = board[r][c]
    baser, basec = r, c
    visits = []
    rainbows = 0
    rainbowCoords = []
    while stack:
        r, c = stack.pop()
        visits.append((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] not in (base, 0):
                continue
            if board[nr][nc] == 9:
                continue
            stack.append((nr, nc))
            visited[nr][nc] = True
            if board[nr][nc] == 0:
                rainbows += 1
                rainbowCoords.append((nr, nc))
    if len(visits) > 1:
        return (len(visits), visits, rainbows, [baser, basec]), rainbowCoords
    else:
        return (), rainbowCoords


def removeBlocksAndGetScore(coords):
    global board
    for r, c in coords:
        board[r][c] = 9


def gravitate(board):
    n, m = len(board), len(board[0])
    for c in range(m):
        row = []
        for r in range(n-1, -1, -1):
            row.append(board[r][c])
        row = moveLeft(row)
        for r, elem in zip(range(n-1, -1, -1), row):
            board[r][c] = elem
    return board


def moveLeft(row):
    for i in range(len(row)):
        if row[i] == -1:
            continue
        j = i
        while j > 0 and row[j-1] == EMPTY:
            row[j-1], row[j] = row[j], row[j-1]
            j -= 1
    return row


def rotateM90(board):
    return list(map(list, zip(*board)))[::-1]


# while 블록 그룹이 존재할 때 까지:
T = 0
while True:
    visited = [[False for _ in range(N)] for __ in range(N)]
    data = []
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            if board[r][c] in (-1, 0, 9):
                continue
            # 그룹 크기, 블록 좌표들, 무지개 수, 기준 블록의 좌표
            ret, rainbowCoords = dfs(r, c, visited)
            if ret != ():
                data.append(ret)
            for rr, cc in rainbowCoords:
                visited[rr][cc] = False
    if data == []:
        break
    data.sort(key=lambda x: (-x[0], -x[2], -x[3][0], -x[3][1]))
    # print(data)
    targetGroup = data[0]
    groupCoords = targetGroup[1]
    # print(groupCoords)
    removeBlocksAndGetScore(groupCoords)
    cnt += targetGroup[0]**2
    # print(board)
    board = gravitate(board)
    # pnt()
    # print("G")
    board = rotateM90(board)
    # pnt()
    # print("R")
    board = gravitate(board)
    # pnt()
    # print("G")
    # print(cnt)
    # T += 1
    # if T == 2:
    # exit()
print(cnt)

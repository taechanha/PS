# 1. 모든 구름 d 방향 s 만큼 이동
# 칸 넘어가면 처리
# 이동 후, 그 자리에 +1
# * 구름 사라짐
# 1-1. 물복사버그
# 대각선 방향에 물이 있는지 체크, 있으면 그 개수만큼 현재 바구니에 +
# 칸 넘어가는 건 안 침
# 2. 물의 양이 2 이상인 모든 칸에 구름, 물의 양은 -2
# * 에서 구름 사라진 칸은 구름 안 생김

def pnt(board):
    for row in board:
        print(row)


def getWaterSum():
    global board, n
    cnt = 0
    for r in range(n):
        for c in range(n):
            if isinstance(board[r][c], tuple):
                cnt += board[r][c][0]
            else:
                cnt += board[r][c]
    return cnt


def getCloudsPos():
    pos = []
    for r in range(n):
        for c in range(n):
            if isinstance(board[r][c], tuple):
                pos.append((r, c))
    return pos


def filterPos(r, c):
    global n
    nr, nc = r, c
    if r < 0:
        nr = n-1
    if c < 0:
        nc = n-1
    if r > n-1:
        nr = 0
    if c > n-1:
        nc = 0
    return nr, nc


def moveAndAdd(di, si, cloudsPos):
    global board, n, dirs
    # 겹치는 경우 방지 위해 새로운 보드
    temp = [row[:] for row in board]
    for r in range(n):
        for c in range(n):
            if isinstance(temp[r][c], tuple):
                temp[r][c] = temp[r][c][0]
    # 이동
    newCloudsPos = []
    dr, dc = dirs[di]
    for r, c in cloudsPos:
        nr, nc = r, c
        for _ in range(si):
            nr = nr + dr
            nc = nc + dc
            nr, nc = filterPos(nr, nc)
        temp[nr][nc] = (temp[nr][nc]+1, '')
        newCloudsPos.append((nr, nc))
    board = [row[:] for row in temp]
    for r, c in newCloudsPos:
        board[r][c] = board[r][c][0]
    return newCloudsPos


def createCloudsAndMinus2(cloudsPos):
    global n
    for r in range(n):
        for c in range(n):
            if isinstance(board[r][c], tuple):
                continue
            if (r, c) in cloudsPos:
                continue
            if board[r][c] > 1:
                board[r][c] = (board[r][c]-2, '')


def copyBug(newCloudsPos):
    global n
    for r, c in newCloudsPos:
        for dr, dc in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if isinstance(board[nr][nc], tuple):
                if board[nr][nc][0] > 0:
                    board[r][c] = board[r][c]+1
            else:
                if board[nr][nc] > 0:
                    board[r][c] = board[r][c]+1


# init
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
di, si = [], []
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# init cloud
board[n-1][0] = (board[n-1][0], '')
board[n-1][1] = (board[n-1][1], '')
board[n-2][0] = (board[n-2][0], '')
board[n-2][1] = (board[n-2][1], '')

# m times
for mi in range(m):
    di, si = map(int, input().split())
    di -= 1
    # move clouds
    cloudsPos: list = getCloudsPos()
    newCloudsPos: list = moveAndAdd(di, si, cloudsPos)  # se: board
    copyBug(newCloudsPos)    # se
    createCloudsAndMinus2(newCloudsPos)  # se
    newCloudsPos, cloudsPos = None, None         # clean up

ans = getWaterSum()
print(ans)

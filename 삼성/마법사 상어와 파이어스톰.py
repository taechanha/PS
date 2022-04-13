# - 인접 칸에 얼음이 3개, 4개 있지 않으면 현재 칸의 얼음이 1 줄어듬 -> temp_board 활용 필요
# - L = 1이면 2^L x 2^L 칸씩 시계방향 90도 회전

# 답: 1. 남아있는 얼음의 합, 2. 가장 큰 얼음 덩어리의 크기(칸의 개수): 섬 문제랑 똑같.

def rotate(L_i):
    global N
    temp = [[0] * N for _ in range(N)]
    N = len(board)
    LI = 2**(L_i)
    for i in range(0, N, LI):
        for j in range(0, N, LI):
            for r in range(LI):
                for c in range(LI):
                    temp[c + i][LI-1-r + j] = board[r + i][c + j]
    return [row[:] for row in temp]


def out_of_bound(r, c):
    return not(0 <= r < N and 0 <= c < N)


def melt():
    global N
    # 상좌하우
    temp_board = [row[:] for row in board]
    N = len(board)
    for r in range(N):
        for c in range(N):
            ice_cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if out_of_bound(nr, nc):
                    continue
                if board[nr][nc] > 0:
                    ice_cnt += 1
            #
            if not(ice_cnt >= 3):
                temp_board[r][c] = max(0, board[r][c] - 1)
    return temp_board


def dfs(r, c, visited):
    stack = [(r, c)]
    visited[r][c] = True
    cnt = 1
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if out_of_bound(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] <= 0:
                continue
            stack.append((nr, nc))
            visited[nr][nc] = True
            cnt += 1

    return cnt


global dr, dc, n, q, board, L, N
n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int, input().split()))
N = 2**n
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# print(sum(map(sum, board)))
for i in range(len(L)):
    # 시계 방향 회전: 2^L 기준으로 [v]
    board = rotate(L[i])
    # 얼음 줄어들기 []
    board = melt()

# 1. 남아있는 얼음의 양
print(sum(map(sum, board)))
# 2. 가장 큰 얼음 덩어리의 크기
visited = [[False] * N for _ in range(N)]
max_size = -float('inf')
for r in range(N):
    for c in range(N):
        if visited[r][c]:
            continue
        if board[r][c] <= 0:
            continue
        ice_size = dfs(r, c, visited)
        max_size = max(max_size, ice_size)
print(max_size)


# board = [[1, 2, 3, 4, 5, 6, 7, 8],
#  [9, 10, 11, 12, 13, 14, 15, 16],
#  [17, 18, 19, 20, 21, 22, 23, 24],
#  [25, 26, 27, 28, 29, 30, 31, 32],
#  [33, 34, 35, 36, 37, 38, 39, 40],
#  [41, 42, 43, 44, 45, 46, 47, 48],
#  [49, 50, 51, 52, 53, 54, 55, 56],
#  [57, 58, 59, 60, 61, 62, 63, 64]]

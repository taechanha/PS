# 4:58 ~ 5:18


# A = 1 2 3 4
#     5 6 7 8

# B = 1 2 3 4 0
#     5 7 9 11 4
#     0 5 6 7 8


# 1. 좌표: 값 배열 세팅
# 2. X, Y 만큼 각 좌표에 값 더해주기 -> 이동 의미
# 3. 각 좌표 돌면서 기존 배열 값 - 좌표 값
# 4. 기존 배열 H W 크기만큼 리턴

H, W, X, Y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H+X)]

coord2val = []
for r in range(H):
    for c in range(W):
        coord2val.append((r+X, c+Y, board[r][c]))

for nr, nc, val in coord2val:
    board[nr][nc] -= val

ans = [[0] * W for _ in range(H)]
for r in range(H):
    for c in range(W):
        ans[r][c] = board[r][c]

for row in ans:
    print(*row)

# 3 3 2 2
# 1 2 3 0 0
# 4 5 6 0 0
# 7 8 10 2 3
# 0 0 4 5 6
# 0 0 7 8 9

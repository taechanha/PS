# 6:23 ~ 6:52 -> failed

def pp(board):
    for row in board:
        print(row)


def fill(R, C, H, W):
    # global n, m
    cand = []
    for r in range(R, R+H):
        for c in range(C, C+W):
            if not (0 <= r < h and 0 <= c < w):
                return 0, True
            if board[r][c]:
                return 0, True
            cand.append((r, c))
    for r, c in cand:
        board[r][c] = 1
    return cand, False


def dfs(i, r, c):
    if not (0 <= r < h and 0 <= c < w):
        return 0
    if i == n:
        return 0
    if board[r][c]:
        return 0
    # i 블록을 현재 위치에 그냥 넣기 or 회전해서 넣기 or 넣지 않기
    case1 = case2 = case3 = 0
    for r in range(r, h):
        for c in range(c, w):
            # 넣기
            cand, err = fill(r, c, coords[i][0], coords[i][1])
            if not err:
                case1 = dfs(i+1, r, c+1) + (coords[i][0] * coords[i][1])
                for rr, cc in cand:
                    board[rr][cc] = 0
            # 회전해서 넣기
            cand, err = fill(r, c, coords[i][1], coords[i][0])
            if not err:
                case2 = dfs(i+1, r, c+1) + (coords[i][0] * coords[i][1])
                for rr, cc in cand:
                    board[rr][cc] = 0
            # 넣지 않기
            case3 = dfs(i+1, r, c+1)
    return max(case1, case2, case3)


coords = []
h, w = map(int, input().split())
board = [[0] * w for _ in range(h)]
n = int(input())
for _ in range(n):
    ri, ci = map(int, input().split())
    coords.append((ri, ci))

res = dfs(0, 0, 0)

print(res)

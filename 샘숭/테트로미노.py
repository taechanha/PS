# 테트로미노를 하나만 놓아서 놓여진 칸의 수의 합이 최대가 되게끔

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 4 * (5 * 20 * 500)
tets = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
]


def moveAndSum(r, c, path):
    global n, m, board
    cnt = 0
    for dr, dc in path:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < n and 0 <= nc < m):
            return 0
        cnt += board[nr][nc]
    return cnt


max_cnt = 0
# 각 테트로미노에 대해
for tet in tets:
    cnt = 0
    # 각 위치에 대해
    for r in range(n):
        for c in range(m):
            max_cnt = max(max_cnt, moveAndSum(r, c, tet))
            max_cnt = max(max_cnt, moveAndSum(r, c, [(-x, y) for x, y in tet]))
            max_cnt = max(max_cnt, moveAndSum(r, c, [(x, -y) for x, y in tet]))
            max_cnt = max(max_cnt, moveAndSum(
                r, c, [(-x, -y) for x, y in tet]))
            rev = [(y, x) for x, y in tet]
            max_cnt = max(max_cnt, moveAndSum(r, c, rev))
            max_cnt = max(max_cnt, moveAndSum(r, c, [(-x, y) for x, y in rev]))
            max_cnt = max(max_cnt, moveAndSum(r, c, [(x, -y) for x, y in rev]))
            max_cnt = max(max_cnt, moveAndSum(
                r, c, [(-x, -y) for x, y in rev]))

print(max_cnt)

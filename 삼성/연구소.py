from itertools import combinations

def get_walls():
    global board
    empty_cells = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                empty_cells.append((i, j))

    return list(combinations(empty_cells, 3))

def spread_virus(r, c):
    global visited
    stack = [(r, c)]
    visited.append((r, c))
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if (nr, nc) in visited:
                continue
            if board[nr][nc] != 0:
                continue
            stack.append((nr, nc))
            visited.append((nr, nc))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
max_cnt = 0
walls = get_walls()
wall_cnt = sum([row.count(1) for row in board]) + 3
nm = n*m

# 벽 세우기
for wall in walls:
    # set wall
    for r, c in wall:
        board[r][c] = 1
    # 안전 영역의 크기 구하기
    visited = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and (i, j) not in visited:
                spread_virus(i, j)

    cnt = nm - len(visited) - wall_cnt
    max_cnt = max(max_cnt, cnt)

    for r, c in wall:
        board[r][c] = 0

print(max_cnt)

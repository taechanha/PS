def out_of_bound(r, c):
    return not (1 <= r < n - 1 and 1 <= c < m - 1)

def dfs(r, c, prev_dir, cnt, visited):
    global min_cnt
    if board[r][c] == 'O':
        min_cnt = min(min_cnt, cnt)

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]

        if out_of_bound(nr, nc):
            continue
        if board[nr][nc] == '#':
            continue
        if (nr, nc) in visited:
            continue
        # 방향 전환: cnt + 1
        # else: cnt
        visited.append((nr, nc))
        if prev_dir == dir:
            dfs(nr, nc, dir, cnt, visited)
        else:
            dfs(nr, nc, dir, cnt+1, visited)
        visited.pop()


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [input() for _ in range(n)]
r, c = -1, -1
min_cnt = float('inf')
print(board)

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            r, c = i, j

dfs(r, c, -1, 0, [])

print(min_cnt)


def dfs(r, c, visited):
    stack = [(r, c)]
    visited[r][c] = True
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] <= 0:
                continue
            stack.append((nr, nc))
            visited[nr][nc] = True


t = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_val = max(map(max, board))
    max_cnt = 0
    for d in range(1, max_val+2):
        visited = [[False] * n for _ in range(n)]
        cnt = 0
        for r in range(n):
            for c in range(n):
                if visited[r][c]:
                    continue
                if board[r][c] <= 0:
                    continue
                dfs(r, c, visited)
                cnt += 1
        max_cnt = max(max_cnt, cnt)
        for r in range(n):
            for c in range(n):
                board[r][c] -= 1

    print(f"#{i+1}", max_cnt)

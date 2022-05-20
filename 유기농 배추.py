def dfs(i, j):
    global visited, row, col, dr, dc
    S = [(i, j)]
    visited[i][j] = 1
    while S:
        r, c = S.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < row and 0 <= nc < col):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == 0:
                continue
            S.append((nr, nc))
            visited[nr][nc] = 1


t = int(input())
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

while t:
    t -= 1

    col, row, k = map(int, input().split())
    board = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    cnt = 0

    for _ in range(k):
        c, r = map(int, input().split())
        board[r][c] = 1

    for i in range(row):
        for j in range(col):
            if visited[i][j]:
                continue
            if board[i][j] != 1:
                continue
            dfs(i, j)
            cnt += 1

    print(cnt)

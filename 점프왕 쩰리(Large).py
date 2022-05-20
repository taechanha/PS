# 11:25 ~ 11:34

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def dfs(r, c):
    stack = [(r, c)]
    visited = [[False] * n for _ in range(n)]
    while stack:
        r, c = stack.pop()
        if (r, c) == (n-1, n-1):
            return True
        val = board[r][c]
        dr, dc = [(val, 0), (0, val)]
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc]:
                continue
            stack.append((nr, nc))
            visited[nr][nc] = True
    return False


print("HaruHaru") if dfs(0, 0) else print("Hing")

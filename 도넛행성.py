def solution(N, M, board):
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    
    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                continue
            if board[r][c] == 1:
                continue
            
            dfs(r, c, visited)
            cnt += 1

    return cnt


def dfs(r, c, visited):
    global N, M, board
    stack = [(r, c)]
    visited[r][c] = True
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            nr = determine('r', nr)
            nc = determine('c', nc)
            
            if visited[nr][nc]:
                continue
            if board[nr][nc] == 1:
                continue
            
            stack.append((nr, nc))
            visited[nr][nc] = True


def determine(kind, pos):
    if kind == 'r':
        boundary = N-1
    else:
        boundary = M-1
    if pos > boundary:
        return 0
    if pos < 0:
        return boundary
    return pos


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = solution(N, M, board)
print(ans)

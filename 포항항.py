# 5:37 ~

# 4 4
# SKKK
# X..X
# X..X
# K..K
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
# dirs = [
#     [[-1, 1, 0, 0], [0, 0, -1, 1]],
#     [[1, -1, 0, 0], [0, 0, -1, 1]],
#     [[-1, 1, 0, 0], [0, 0, 1, -1]],
#     [[1, -1, 0, 0], [0, 0, 1, -1]],
# ]

# assert n_restaurants == 5

# dfs + bfs


# def dfs(r, c, time, k):
#     if k == 5:
#         return time

#     min_time = float('inf')
#     for i in range(4):
#         dist, arrv_r, arrv_c = bfs(r, c, *dirs[i])
#         if dist == -1:
#             continue
#         board[arrv_r][arrv_c] = '.'
#         min_time = min(min_time, dfs(arrv_r, arrv_c, time+dist, k+1))
#         board[arrv_r][arrv_c] = 'K'
#     return min_time


def bfs(r, c, dr, dc):
    que = [(r, c, 0)]
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    cnt = 0
    total_dist = 0
    while que:
        r, c, dist = que.pop(0)
        if board[r][c] == 'K':
            visited[r][c] = False
            board[r][c] = '.'
            cnt += 1
            total_dist += dist
            if cnt == 5:
                return total_dist
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == 'X':
                continue
            que.append((nr, nc, dist+1))
            visited[nr][nc] = True
    return -1


dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

pos_s = None
n_restaurants = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            pos_s = (i, j)
        if board[i][j] == 'K':
            n_restaurants += 1

if n_restaurants < 5:
    print(-1)
    exit(0)
r, c = pos_s  # s's position
dist = bfs(r, c, dr, dc)
print(dist)

# min_time = dfs(r, c, 0, 0)
# print(-1) if min_time == float('inf') else print(min_time)

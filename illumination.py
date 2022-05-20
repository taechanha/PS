from collections import deque


def is_in_boundary(x, y):
    return 0 <= x < h and 0 <= y < w


def bfs(G, x, y):
    q = deque([[x, y]])
    visited = [[False for __ in range(w)] for _ in range(h)]
    visited[x][y] = True
    count = 0

    while q:
        current_x, current_y = q.popleft()

        for i in range(len(dx)):
            nx = current_x + dy[i]
            ny = current_y + dx[i]

            if not is_in_boundary(nx, ny):
                continue

            if visited[nx][ny]:
                continue

            if G[nx][ny] == '1':
                q.append([nx, ny])
                visited[nx][ny] = True
            else:
                if G[current_x][current_y] == '1':
                    count += 1

    return count


w, h = map(int, input().split())

grid = [list(input().split()) for _ in range(h)]

# left_down, right_down, right, left, left_up, right_up
dx = [0, 1, 0, 0, -1, 0]
dy = [1, 1, 1, -1, -1, -1]

print(bfs(grid, 0, 0))


# 8 4
# 0 0 0 0 0 0 0 0 0 0
# 0 0 1 0 1 0 1 1 1 0
# 0 0 1 1 0 0 1 0 0 0
# 0 1 0 1 0 1 1 1 1 0
# 0 0 1 1 0 1 0 1 0 0
# 0 0 0 0 0 0 0 0 0 0

# 4 6
# 1 0 1 1 1 1
# 1 0 1 0 1 0
# 1 0 1 0 1 1
# 1 1 1 0 1 1
from collections import deque


def is_beyond_limit(x, y):
    return x < 0 or x > n - 1 or y < 0 or y > m - 1


def is_zero(x, y):
    return arr[x][y] == 0


def bfs(n, m):
    # init q
    q = deque([(0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()

        if (x, y) == (n-1, m-1):
            return visited[n-1][m-1]

        for dx, dy in zip(nx, ny):
            if not is_beyond_limit(x + dx, y + dy):
                if visited[x + dx][y + dy] == 0 and not is_zero(x + dx, y + dy):
                    q.append((x + dx, y + dy))
                    visited[x + dx][y + dy] = visited[x][y] + 1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

print(bfs(n, m))

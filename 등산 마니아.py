# 8:19 ~
import sys
sys.setrecursionlimit(10**6)

n = int(input())
for _ in range(n-1):
    a, b = input().split()

# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
min_cost = float('inf')


def dfs(r, c, cost, path):
    global min_cost
    # base case
    if (r, c) == (n-1, n-1):
        min_cost = min(min_cost, cost)
        # if min_cost == cost:
        # print(path, cost)
        return
    # explore
    # either right or down
    for dr, dc in (0, 1), (1, 0):
        nr, nc = r+dr, c+dc
        # if (nr, nc) == (2, 2):
        # a = 1
        if not (0 <= nr < n and 0 <= nc < n):
            continue
        if visited[nr][nc]:
            continue
        diff = 0
        if board[nr][nc] >= board[r][c]:
            diff = (board[nr][nc] + 1 - board[r][c])
        visited[nr][nc] = True
        # path.append((nr, nc))
        dfs(nr, nc, cost+diff, path)
        # path.pop()
        visited[nr][nc] = False


dfs(0, 0, 0, [])
visited[0][0] = True
print(min_cost)

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
m = len(grid)
n = len(grid[0])


# bottom-up
M, N = len(grid), len(grid[0])
cost = [[0]*N for _ in range(M)]
cost[0][0] = grid[0][0]
for j in range(1,N):
    cost[0][j] = grid[0][j] + cost[0][j-1]
for i in range(1,M):
    cost[i][0] = grid[i][0] + cost[i-1][0]
for i in range(1,M):
    for j in range(1,N):
        cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]

print(cost[M-1][N-1])


# top-down
# dp = [[-1] * n for _ in range(m)]
# dp[m-1][n-1] = grid[m-1][n-1]

# def dfs(x, y):
#     if x == m or y == n:
#         return float('inf')
#     else:
#         if dp[x][y] != -1:
#             return dp[x][y]
#         else:
#             right = dfs(x, y + 1) + grid[x][y]
#             left = dfs(x + 1, y) + grid[x][y]
#             dp[x][y] = min(right, left)
#             return dp[x][y]


# print(dfs(0, 0))

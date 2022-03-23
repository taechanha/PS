import sys
input = sys.stdin.readline


def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        x1, y1 = x + s[x][y], y
        x2, y2 = x, y + s[x][y]
        if 0 <= x1 < n and 0 <= y1 < n:
            dp[x][y] += dfs(x1, y1)
        if 0 <= x2 < n and 0 <= y2 < n:
            dp[x][y] += dfs(x2, y2)
    return dp[x][y]


n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
dp = [[-1] * n for i in range(n)]
print(dfs(0, 0))

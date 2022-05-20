
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        def dfs(i, j):
            if i >= row or j >= col or obstacleGrid[i][j] == 1:
                return 0
            if i == row-1 and j == col-1:
                return 1

            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i, j+1) + dfs(i+1, j)
            return memo[i][j]

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        memo = [[-1] * col for _ in range(row)]
        return dfs(0, 0)


s = Solution()
tc1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
tc2 = [[0, 1], [0, 0]]
res = s.uniquePathsWithObstacles(tc1)
print(res)

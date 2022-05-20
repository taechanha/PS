from collections import defaultdict


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def dfs(r, c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1
            if (r, c, k) in memo:
                return memo[(r, c, k)]
            cases = 0
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                cases += dfs(nr, nc, k-1)
            memo[(r, c, k)] = cases
            return memo[(r, c, k)]

        #     1,  2, 4,  5, 7, 8,  9, 10
        memo = dict()
        dr = [-2, -1, 1, 2, 2, 1, -1, -2]
        dc = [1, 2, 2, 1, -1, -2, -2, -1]
        return dfs(row, column, k) / 8**k


# Return the probability that the knight remains on the board after it has stopped moving.
n = 3
k = 2
row = 0
column = 0
s = Solution()
res = s.knightProbability(n, k, row, column)
print(res)
# 3
# 2
# 0
# 0
# my answer = 0.0
# expected = 0.0625

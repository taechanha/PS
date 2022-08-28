from collections import defaultdict
from functools import cache, lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(i, j, moves_left):
            if not(0 <= i < m and 0 <= j < n):
                return 1
            if moves_left == 0:
                return 0
            cnt = 0
            for idx in range(4):
                nr = i + dr[idx]
                nc = j + dc[idx]
                cnt += dfs(nr,
                           nc, moves_left-1) % 1_000_000_007
            return cnt

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        return dfs(startRow, startColumn, maxMove)


m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
# m = 1
# n = 3
# maxMove = 3
# startRow = 0
# startColumn = 1
# m = 8
# n = 50
# maxMove = 23
# startRow = 5
# startColumn = 26
s = Solution()
res = s.findPaths(m, n, maxMove, startRow, startColumn)

print(res)

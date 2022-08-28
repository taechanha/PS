# class Solution:
#     def tilingRectangle(self, n: int, m: int) -> int:
#         def dfs(i, j):
#             if i == j:
#                 return 1
#             # 0이거나 이하일 수 없음,
#             #   1) 0인 경우는 두 수가 같은 경우 -> 위 cond에서 커버,
#             #   2) 0 이하는 왜 안되냐면, 더 큰 수로 작은 수를 빼는 것이기 때문
#             if i == 1 and j == 1:
#                 return 1
#             i, j = max(i, j), min(i, j)
#             return dfs(j, i - j) + dfs(j, j)

#         if (n == 11 and m == 13) or (n == 13 and m == 11):
#             return 6
#         return dfs(n, m)
# dp = [[0] * (m + 1) for _ in range(n + 1)]
# if (n == 11 and m == 13) or (n == 13 and m == 11):
#     return 6
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if i == j:
#             dp[i][j] = 1
#             continue
#         dp[i][j] = i * j
#         for k in range(i // 2 + 1):
#             dp[i][j] = min(dp[i][j], dp[i-k][j] + dp[k][j])
#         for k in range(j // 2 + 1):
#             dp[i][j] = min(dp[i][j], dp[i][j-k] + dp[i][k])
# return dp[-1][-1]
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = m * n

        def dfs(height, moves):
            if all(h == n for h in height):
                self.best = min(self.best, moves)
                return
            if moves >= self.best:
                return
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                new_height = height[:]
                for j in range(i):
                    new_height[idx + j] += i
                dfs(new_height, moves + 1)

        dfs([0] * m, 0)
        return self.best


n = 2
m = 3
s = Solution()
res = s.tilingRectangle(n, m)
print(res)

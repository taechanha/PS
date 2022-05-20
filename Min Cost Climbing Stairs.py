class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        cost += [0]
        dp = [0] * n + [0]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        print(dp)
        return dp[-1]


cost = [10, 15, 20]
cost = [1,100,1,1,1,100,1,1,100,1]
s = Solution()
res = s.minCostClimbingStairs(cost)
print(res)

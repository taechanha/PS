test = [1, -3, 4, -1, -5]


class Solution:
    def maxSubArray(self, nums) -> int:
        # sub-problem: dp[i] = max sum of nums[i:]
        # relate: dp[i] = max{ dp[i+1:] + nums[i], dp[i+1:] }
        def dfs(i):
            if i == len(nums) - 1:
                dp[i] = nums[i]
                return dp[i]
            if dp[i] != 0:
                return dp[i]
            dp[i] = max(dfs(i+1) + nums[i], nums[i])
            return dp[i]

        dp = [0] * len(nums)
        dfs(0)
        return max(dp)


sol = Solution()
print(sol.maxSubArray(test))
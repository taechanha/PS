from functools import cache, lru_cache
# 1. dfs + backtrack


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @lru_cache
        def dfs(nums, rest, chosen):
            if rest < 0:
                return 0
            elif rest == 0:
                return 1

            cnt = 0
            for i in range(len(nums)):
                rest -= nums[i]
                chosen += str(nums[i])
                cnt += dfs(nums, rest, chosen)
                rest += nums[i]
            return cnt

        return dfs(nums, target, "")

# 2. bottom up


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        
        for t in range(1, target + 1):
            for i in range(len(nums)):
                if t - nums[i] < 0:
                    break
                dp[t] += dp[t - nums[i]]

        return dp[target]


nums = [1, 2, 3]
target = 4
# nums = [4, 2, 1]
# target = 32
# nums = [2, 3, 4]
# target = 4
s = Solution()
res = s.combinationSum4(nums, target)

print(res)

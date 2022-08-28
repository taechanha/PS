# 1. 완탐
# 2. two-pointers
# 3. dp
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        def dfs(chosen, start):
            if start == len(nums):
                return False
            if chosen == (sum(nums) - chosen):
                return True

            for i in range(start, len(nums)):
                chosen += nums[i]
                ans = dfs(chosen, i+1)
                if ans == True:
                    return True
                chosen -= nums[i]
            return ans

        return dfs(0, 0)


nums = [1, 5, 11, 5]
nums = [1, 2, 3, 5]
s = Solution()
res = s.canPartition(nums)

print(res)

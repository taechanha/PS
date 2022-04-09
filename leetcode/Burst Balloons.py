from typing import List


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        global n
        def X(nums, i, j):
            global n
            if i > j:
                return 0
            if i == j:
                temp = nums[i]
                if i - 1 >= 0:
                    temp *= nums[i-1]
                if i + 1 < n:
                    temp *= nums[i+1]
                return temp
            if dp[i][j] != -1:
                return dp[i][j]
            ans = 0
            for k in range(i, j+1):
                temp = nums[k]
                if j + 1 < n:
                    temp *= nums[j+1]
                if i - 1 >= 0:
                    temp *= nums[i-1]
                temp += X(nums, i, k-1) + X(nums, k+1, j)
                ans = max(ans, temp)
                dp[i][j] = ans

            return dp[i][j]

        dp = [[-1] * 501 for _ in range(501)]
        nums = [1] + nums + [1]
        n = len(nums)
        return X(nums, 1, n-2)


nums = [3, 1, 5, 8]
s = Solution()
res = s.maxCoins(nums)
print(res)

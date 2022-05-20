class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        max_len = 0
        lens = [0] * n
        cnts = [0] * n
        for i in range(0, n):
            lens[i] = cnts[i] = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if lens[i] == lens[j] + 1:
                        cnts[i] += cnts[j]
                    elif lens[i] < lens[j] + 1:
                        lens[i] = lens[j] + 1
                        cnts[i] = cnts[j]
            if max_len == lens[i]:
                res += cnts[i]
            elif max_len < lens[i]:
                max_len = lens[i]
                res = cnts[i]

        return res


nums = [1, 3, 5, 4, 7]
s = Solution()
res = s.findNumberOfLIS(nums)
print(res)

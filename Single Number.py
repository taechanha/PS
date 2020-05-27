class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = Counter(nums)
        for idx, val in a.items():
            if val == 1:
                return idx
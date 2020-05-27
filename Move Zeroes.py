class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = []
        for idx, n in enumerate(nums):
            if n == 0:
                zeros.append(idx)
                continue
            if(len(zeros) != 0):
                nums[zeros.pop(0)] = n
                nums[idx] = 0
                zeros.append(idx)
                
        
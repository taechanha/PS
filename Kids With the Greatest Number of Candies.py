import numpy as np
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        res = []
        for i in candies:
            i += extraCandies
            if(i >= maximum):
                res.append(1)
            else:
                res.append(0)
        return res
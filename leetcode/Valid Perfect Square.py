class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1
        while(1):
            if x*x == num:
                return 1
            if x*x >= pow(2, 31) :
                return 0
            x += 1
            
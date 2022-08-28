class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def LIS(start): 
            max_len = 0
            if start == n - 1:
                return 0
            if dp[start] != 0:
                return dp[start]
            for i in range(start + 1, n):
                if nums[start] < nums[i]:
                    #return LIS(i) + 1 # 여기서 리턴하면 1 -> 3, 3 함수에서 리턴되고 1 -> 2가 진행이 안된다.
                    max_len = max(max_len, LIS(i) + 1)
                    dp[start] = max_len
            return dp[start]
                    
        n = len(nums)
        dp = [0] * n
        max_len = 0 # input이 [0]인 경우, for 문을 통과하지 않고 바로 리턴함. 0을 리턴하면 안 되니까 1로 초기화해준다.
        for i in range(len(nums)):
            max_len = max(max_len, LIS(i) + 1)
        return max_len
                    
# sub-problem: LIS(i) = LIS(A[i:]) 라고 정의하면,
# 비교가 이루어지지 않아 Increasing 조건을 부여하지 못함
# 비교를 하려면, 현재 위치와, 이전에 넣은 위치를 기억하고 있어야함
# 하지만 현재의 sub-problem 정의로는 이전에 넣은 위치를 기억할 수 없음
# sub-problem 정의를 바꾸자.
# sub-problem: LIS(i) = LIS(A[i:]) - i를 시작으로 하는 A에서의 LIS
# relate: LIS(i) = 1 + max{ LIS(j) | i < j < n, A[i] < A[j]} u { 0 }

#     01234                    
# Ex. CARBO, n = 5, answer would be ABO => LIS(s) = 3
# start from 0                     
# LIS(0) = 1 + max{ LIS(j) | 0 < j <= n, A[i] < A[j] }                   j = 1, C
#        = 1 + 1 + max{ LIS(j) | 2 < j <= n, A[i] < A[j] }               j = 2, CR
#           = ...                    
#           = j == n => END
             
#        = 1 + 1 + max{ LIS(j) | 4 < j <= n, A[i] < A[j] }               j = 4, CO

# LIS(1) = 1 + max{ LIS(j) | 1 < j <= n, A[i] < A[j] }                   j = 1, A
#           = 1 + max{ LIS(j) | 2 < j <= n, A[i] < A[j] }                j = 2, AR
#               = ...
#               = j == n => END
                   
#           = 1 + 1 + max{ LIS(j) | 4 < j <= n, A[i] < A[j] }            j = 3, AB
#               = 1 + 1 + 1 + max{ LIS(j) | 5 < j <= n, A[i] < A[j] }    j = 4, ABO
#               = j == n => END

# LIS(2) = ...                   
                  
                 
                   
                   
                   

                    
                    
                    
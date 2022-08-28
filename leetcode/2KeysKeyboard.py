import math


class Solution:
    def minSteps(self, n: int) -> int:
        def is_prime(n):
            # Corner case
            if (n <= 1):
                return False

            # Check from 2 to sqrt(n)
            for i in range(2, int(math.sqrt(n))+1):
                if (n % i == 0):
                    return False

            return True

        def helper(n):
            if n == 1:
                return 0
            if dp[n] != -1:
                return dp[n]
            if is_prime(n):
                dp[n] = n
                return n
            else:
                for biggest_divisor in range(n - 1, 1, -1):
                    if n % biggest_divisor == 0:
                        dp[n] = n // biggest_divisor + helper(biggest_divisor)
                        return dp[n]

            # if prime; return the number
            # else; number//biggest_divisor + helper(number)

            # 원래 작성했던 코드. RHS 검증을 하자^^
            # dp[n] = min(helper(n//2) + 2, helper(n-2) + 2)
            # return dp[n]

        dp = [-1] * (n + 1)
        return helper(n)


s = Solution()
res = s.minSteps(7)
print(res)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * 21
        dp[0], dp[1] = 1, 1

        # for level in range(2, n+1):
        #     for root in range(1, level+1):
        #         dp[level] += dp[level-root] * dp[root-1]
        #         if level == n:
        #             print(dp[level], level-root, root-1)

        for i in range(2, n + 1):
            for k in range(0, i):
                dp[i] += dp[k] * dp[i-1-k]
                # if i == 3:
                # print(dp[i], k, n-1-k)
            # print(dp)
        print(dp)
        return dp[n]


n = 6
s = Solution()
res = s.numTrees(n)
print(res)

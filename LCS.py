
def longestCommonSubsequence(text1: str, text2: str) -> int:
    def LCS(i, j):
        if i == n or j == m:
            return 0
        else:
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = LCS(i+1, j+1) + 1
            else:
                dp[i][j] = max(LCS(i, j+1), LCS(i+1, j))

            return dp[i][j]

    n = len(text1)
    m = len(text2)
    dp = [[-1] * m for _ in range(n)] # dp[n][m]
    return LCS(0, 0)


# n = 5, m = 3
#   a c e
# a
# b
# c
# d
# e
print(longestCommonSubsequence("abcde", "ace"))

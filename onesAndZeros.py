def helper(ones_left, zeros_left, step):
    if ones_left == 0 and zeros_left == 0:
        return 0
    if ones_left < 0 or zeros_left < 0:
        return -float('inf')
    if step == len(strs):
        return 0
    if dp[step] != -float('inf'):
        return dp[step]
    ones, zeros = counter[step]
    dp[step] = max(helper(ones_left-ones, zeros_left-zeros,
                   step+1) + 1, helper(ones_left, zeros_left, step+1))
    return dp[step]


strs = ["10", "0", "1"]
m = 1
n = 1

counter = [[s.count('1'), s.count('0')] for s in strs]
dp = [-float('inf')] * len(strs)
helper(n, m, 0)
print(dp)


# class Solution:
#   def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#     dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
#     for s in strs:
#       freqs = Counter(s)
#       zeros, ones = freqs['0'], freqs['1']

#       for i in range(m, zeros - 1, -1):
#         for j in range(n, ones - 1, -1):
#           dp[i][j] = max(1 + dp[i - zeros][j - ones], dp[i][j])

#     return dp[m][n]

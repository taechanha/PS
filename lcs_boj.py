import sys
sys.setrecursionlimit(10**6)

# dp = [[-1] * m for _ in range(n)]


# def X(i, j):
#     if i == n or j == m:
#         return 0

#     if dp[i][j] != -1:
#         return dp[i][j]

#     if s[i] == t[j]:
#         dp[i][j] = X(i+1, j+1) + 1
#     else:
#         dp[i][j] = max(X(i, j+1), X(i+1, j))

#     return dp[i][j]


# ret = X(0, 0)
# print(ret)

# X(i, j): s[:i]와 t[:j]의 최장 공통 부분수열



# bottom-up

s = input()
t = input()
n = len(s)
m = len(t)

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
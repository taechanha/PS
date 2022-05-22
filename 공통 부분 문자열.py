# 11:33 ~
from functools import lru_cache

s = input()
t = input()
n, m = len(s), len(t)


import sys
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

dp = [[0] * len(T) for _ in range(len(S))]
answer = 0

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
            answer = max(answer, dp[i][j])

print(answer)


# dp = [[-1] * (m + 1) for _ in range(n + 1)]
res = lcs(n, m, 0)
print(res)


# RACADABRA
# DADABRBCR

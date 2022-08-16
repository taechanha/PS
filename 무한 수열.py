N, P, Q = map(int, input().split())

# => 메모리 초과
# A = [1] + ([0] * N)
# for i in range(1, N+1):
#     A[i] = A[i//P] + A[i//Q]

dp = {}


def dfs(n):
    if n == 0:
        return 1
    if n in dp:
        return dp[n]
    dp[n] = dfs(n//P) + dfs(n//Q)
    return dp[n]


print(dfs(N))

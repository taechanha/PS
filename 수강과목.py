def KS(n, C):
    if n == 0 or C == 0:
        return 0

    if dp[n-1][C] != -1:
        return dp[n-1][C]

    case1 = case2 = 0
    if weights[n-1] > C:
        case1 = KS(n-1, C)
        dp[n-1][C] = case1
        return case1

    case1 = KS(n-1, C)
    case2 = KS(n-1, C-weights[n-1]) + values[n-1]
    dp[n-1][C] = max(case1, case2)
    return dp[n-1][C]


C, K = map(int, input().split())
values = []
weights = []
dp = [[-1] * (C+1) for _ in range(K+1)]

for _ in range(K):
    v, w = map(int, input().split())
    values.append(v)
    weights.append(w)

print(KS(K, C))

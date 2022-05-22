# def dfs(idx, profit, last_added_profit):
#     global max_profit, n
#     if idx == n:
#         max_profit = max(max_profit, profit)
#         return
#     if idx > n:
#         profit -= last_added_profit
#         max_profit = max(max_profit, profit)
#         return
#     for i in range(idx, len(tp)):
#         t, p = tp[i][0], tp[i][1]
#         dfs(i+t, profit+p, p)


def dfs(i):
    global dp
    if i > n:
        return -float('inf')
    if i == n:
        return 0
    if dp[i] != 0:
        return dp[i]
    dp[i] = max(dfs(i+1), dfs(i + tp[i][0]) + tp[i][1])
    return dp[i]


n = int(input())
tp = [list(map(int, input().split())) for _ in range(n)]
max_profit = 0

dp = [0] * n
res = dfs2(0)

print(res)
print(dp)

# dfs(0, 0, 0, [])

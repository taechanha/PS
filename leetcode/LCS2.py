# 6:32 ~

# ACAYKP와 CAPCAK -> ACAK

def dfs(i, j, chosen):
    global max_chosen, max_len
    if i == n or j == m:
        chosen_len = len(chosen)
        if chosen_len > max_len:
            max_len = chosen_len
            max_chosen = chosen
        dy[i][j] = 0
        return 0

    if dy[i][j] != -1:
        return dy[i][j]

    if s[i] == t[j]:
        dy[i][j] = dfs(i+1, j+1, chosen+s[i]) + 1
        return dy[i][j]

    case1 = dfs(i+1, j, chosen)
    case2 = dfs(i, j+1, chosen)
    dy[i][j] = max(case1, case2)
    return dy[i][j]


s = input()
t = input()
n, m = len(s), len(t)
max_chosen = ""
max_len = 0
dy = [[-1] * max(n+1, m+1) for _ in range(max(n+1, m+1))]
res = dfs(0, 0, "")

if res == 0:
    print(0)
else:
    print(max_len)
    print(max_chosen)


# s = input()
# t = input()
# n = len(s)
# m = len(t)

# path = [['O'] * (m+1) for _ in range(n+1)]
# dp = [[0] * (m+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         if s[i-1] == t[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#             path[i][j] = s[i-1]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print(dp[-1][-1])

# if dp[-1][-1] == 0:
#     exit()

# for r in range(n+1):
#     new = ""
#     for c in range(m+1):
#         if not (0 <= c+r < n+1):
#             continue
#         if path[c+r][c] != 'O':
#             new += path[c+r][c]
#     if new:
#         print(new)

# for row in path:
#     print(row)

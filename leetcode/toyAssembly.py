from collections import defaultdict

n = int(input())
m = int(input())

dp = {}
ans = defaultdict(int)

for _ in range(m):
    x, y, k = map(int, input().split())
    if x not in dp:
        dp[x] = [y, k]
    else:
        dp[x] += [y, k]

dp = dict(sorted(dp.items()))


lk = list(dp)[-1]

for i in range(0, len(dp[lk]), 2):
    acc = 0
    key = dp[lk][i]
    print(dp[key])
    for j in range(0, len(dp[key]), 2):
        basic_parts = dp[key][j]
        ans[basic_parts] += dp[key][j+1]

    ans[basic_parts] *= dp[lk][i + 1]

print(dp)
print(ans)

# 5 2 -> 1 2 2 2
# 6 3
# 4 5

# {5: [1, 2, 2, 2], 6: [5, 2, 3, 3, 4, 4], 7: [5, 2, 6, 3, 4, 5]}

n = int(input())
dp = [0] * 1000001

for i in range(2, n + 1):
    dp[i] = 1 + dp[i - 1]
    if i % 3 == 0:
        dp[i] = 1 + min(dp[i // 3], dp[i - 1])
    if i % 2 == 0:
        dp[i] = 1 + min(dp[i // 2], dp[i - 1])

print(dp[n])

# def to_one(n, cnt):
#     if n <= 1:
#         return cnt

#     if dp[n] != 0:
#         return dp[n]
#     else:
#         if n % 3 == 0:
#             dp[n] = to_one(n // 3, cnt + 1)
#         elif n % 2 == 0:
#             dp[n] = to_one(n // 2, cnt + 1)
#         dp[n] = to_one(n - 1, cnt + 1)


# to_one(10, 0)
# print(answer, min(answer))

# 10 5 4 2 1

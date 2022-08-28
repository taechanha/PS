import math


def is_square(n: int) -> bool:
    return (math.sqrt(n) % 1) == 0


def numSquares(n: int) -> int:
    dp = [10001] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        # 1, IF i is square number
        if is_square(i):
            dp[i] = 1
        else:
            # min(dp[j] for j in range(i-1, i//2)), OTHERWISE
            # above is slow. instead, use
            # dp[i - 1] + 1
            # dp[i - 4] + 1
            # dp[i - 9] + 1 ...
            # i:6 -> j's option: (1, 4)
            # i:3 -> j's option: (1)
            # so, j is a square number smaller than i
            # Ex.
            # i: 6
            # j: 1 -> dp[6 - 1*1] + 1
            # j: 2 -> dp[6 - 2*2] + 1
            j = 1
            while j*j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j = j+1

    return dp[n]


res = numSquares(7168)
print(res)


# min_temp = dp[i-1] + dp[1]
# cnt = 1
# for j in range(i-1, i//2-1, -1):  # i=9: j=8, j=7, ..., j=4
# # print(j)
#     min_temp = min(min_temp, dp[i-cnt] + dp[i-j])
#     cnt += 1

# dp[i] = min_temp

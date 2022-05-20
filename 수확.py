import sys
sys.setrecursionlimit(10**6)


def solve():

    n = int(input())
    v = [int(input()) for _ in range(n)]
    dp = [[0] * 2001 for _ in range(2001)]

    def X(l, r, i):
        if l > r:
            "asdadas"
            return 0
        if dp[l][r] != 0:
            return dp[l][r]

        dp[l][r] = max(X(l+1, r, i+1) + (i*v[l]),
                       X(l, r-1, i+1) + (i*v[r]))
        return dp[l][r]

    return X(0, n-1, 1)


print(solve())


# # two pointers approach
# l = 0
# r = n - 1
# i = 1
# profit = 0

# while l < r:
#     if v[l] >= v[r]:
#         profit += v[r] * i
#         r -= 1
#     else:
#         profit += v[l] * i
#         l += 1
#     i += 1

# print(profit + (v[r] * i))

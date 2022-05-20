def solution():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    l, r = 0, 0
    sum = nums[0]
    min_len = n+1

    while l <= r and r < n:
        if sum < s:
            r += 1
            if r >= n:
                continue
            sum += nums[r]

        else:
            min_len = min(min_len, r-l+1)
            sum -= nums[l]
            l += 1

    if min_len == n+1:
        return 0
    return min_len

res = solution()
print(res)


# import sys
# si = sys.stdin.readline
# n, S = list(map(int, si().split()))
# a = list(map(int, si().split()))
# R, sum, ans = -1, 0, n + 1
# for L in range(n):
#     while R + 1 < n and sum < S:
#         R += 1
#         sum += a[R]

#     if sum >= S:
#         ans = min(ans, R - L + 1)

#     sum -= a[L]

# if ans == n + 1: ans = 0
# print(ans)

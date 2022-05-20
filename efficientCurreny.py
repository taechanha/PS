# n, m = input().split()
# cur = [int(input()) for _ in range(n)]
# dp = [0] * 10001

# for each in cur:
#     dp[each] = 1
# # 0 1 2 3 4 5 6
# # 0 0 1 1 2 0 0

# for i in range(4, m + 1):
#     dp[i-2] * 2
#     dp[i-1] + dp[i-2]


#     dp[i] =

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

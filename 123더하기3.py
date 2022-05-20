t = int(input())
mod = 1000000009
limit = 1000001
dp = [0] * limit

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, limit):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % mod

while t:
    t -= 1

    n = int(input())
    
    print(dp[n] % mod)

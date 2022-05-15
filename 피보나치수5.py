def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if dp[n]:
        return dp[n]
    else:
        dp[n] = fib(n - 1) + fib(n - 2)
        
    return dp[n]


n = int(input())
dp = [0] * (n + 1)

print(fib(n))


def coinChange(coins, amount: int) -> int:
    INF = float('inf')
    dp = [0] + [INF] * amount

    for amt in range(1, amount + 1):
        if amt in coins:
            dp[amt] = 1
        else:
            dp[amt] = min([dp[amt - coin] if amt - coin >= 0 else INF for coin in coins]) + 1

            # for i in range(1, amt//2 + 1):
            #     dp[amt] = min(dp[amt], dp[amt-i] + dp[i])

    if dp[amount] == INF:
        return -1
    return dp[amount]

coins = [1]
amount = 0
res = coinChange(coins, amount)
print(res)

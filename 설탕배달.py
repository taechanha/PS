def back(n, cnt):
    if n < 0:
        return -1
    elif n == 0:
        return cnt
    else:
        if dp[n]:
            return dp[n]

        ret1 = back(n - 5, cnt + 1)
        ret2 = back(n - 3, cnt + 1)

        if ret1 == -1:
            if ret2 == -1:
                dp[n] = -1
                return dp[n]
            else:
                dp[n] = ret2
                return dp[n]
        else:
            if ret2 != -1:
                dp[n] = min(ret1, ret2)
                return dp[n]
            else:
                dp[n] = ret1
                return dp[n]

def back(n, cnt=False):
    weight = n
    threes = weight * 2 % 5
    fives = (weight - 3 * threes) / 5
    if fives < 0:
        return -1
    else:
        return threes + fives


def back(n, cnt=False):
    three_pack = 0
    while n % 5:
        three_pack += 1
        n -= 3
    if n < 0:
        return -1
    five_pack = n / 5
    return three_pack + five_pack


def back(n, cnt=False):
    c = 0
    while n % 5 != 0:
        n -= 3
        c += 1
    if n < 0:
        print(-1)
    else:
        print(c + (n // 5))

def back(n, cnt=False):
    for i in range(1, n + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3])
        if i >= 5:
            dp[i] = min(dp[i], dp[i-5])
        
        dp[i] += 1

    if dp[n] > 1e9:
        return -1
    else:
        return dp[n] 

n = int(input())
dp = [0x3f] * 10

print(back(n, 0))

# 5:45 ~ 6:45

import sys
sys.setrecursionlimit(10**7)

N = int(input())

# preprocess
n = 999_999 + 1
a = [False, False] + [True]*(n-1)
primes = set()

for i in range(2, n+1):
    if a[i]:
        primes.add(i)
        for j in range(2*i, n+1, i):
            a[j] = False


def dfs(a, b, cnt):
    concat = int(str(a) + str(b))

    if a > N or b > N:
        dp[concat] = cnt
        return cnt

    if concat in dp:
        return dp[concat]
    
    if (a, b) != (1, 1) and concat in primes:
        cnt += 1

    dp[concat] = max(dfs(a+1, b, cnt), dfs(a, b+1, cnt))
    return dp[concat]

dp = {}
print(dfs(1, 1, 0))


# ANSWER BELOW

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def recur(a, b):
    if a == N and b == N:
        return 0

    if dp[a][b] != -1:
        return dp[a][b]

    case1 = case2 = 0
    if (a, b) != (1, 1) and is_prime[int(str(a) + str(b))]:
        if a < N:
            case1 = recur(a + 1, b) + 1
        if b < N:
            case2 = recur(a, b + 1) + 1
    else:
        if a < N:
            case1 = recur(a + 1, b)
        if b < N:
            case2 = recur(a, b + 1)

    dp[a][b] = max(case1, case2)
    return dp[a][b]


if __name__ == "__main__":
    N = int(input())

    # 소수 전처리
    is_prime = [True for _ in range(1_000_000)]
    for i in range(2, 1000000):
        for j in range(i + i, 1000000, i):
            if not is_prime[j]:
                continue

            is_prime[j] = False

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    print(recur(1, 1))


# check if sum of square of each number of a number ends up with 1
def check(num): # 효율성 문제 있는듯? 후보: 1) str,
    dp = {}
    while num != 1:
        dp[num] = 0
        num = str(num)
        num = sum(map(lambda x: pow(int(x), 2), num))
        if num in dp:
            return False
    return True


def eratostenes(n):  # find prime numbers by eratostenes sieve
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]


n = int(input())
primes = eratostenes(n+1)
ans = []
for prime in primes:
    # check
    if check(prime):
        ans.append(prime)

print(ans)

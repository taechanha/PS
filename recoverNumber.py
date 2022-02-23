from collections import defaultdict


def factorize(n):
    ans = defaultdict(int)
    while not isprime(n):

        for i in range(2, n):
            if not isprime(i):
                continue
            if n % i == 0:
                n //= i
                ans[i] += 1
                break
    ans[n] += 1
    return ans


def print_ans(d: dict):
    for k, v in d.items():
        print(k, v)


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


T = int(input())

while T:
    T -= 1
    n = int(input())
    ans = factorize(n)
    print_ans(ans)

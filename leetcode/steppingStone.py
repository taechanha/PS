# 1
# 4

# 강을 건너는 방법은, (1 → 4), (1 → 2 → 4), (1 → 3 → 4), (1 → 2 → 3 → 4)의 4가지이다
import sys
read = sys.stdin.readline
BIG_NUMBER = 1000000007


def helper(N):
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return power(2, N - 2) % BIG_NUMBER


def power(a, b):
    if b == 0:
        return 1
    tmp = power(a, b // 2)
    result = (tmp * tmp) % BIG_NUMBER
    if b % 2 == 1:
        result = (result * a) % BIG_NUMBER
    return result


def main():
    T = int(read())
    for _ in range(T):
        N = int(read())
        print(helper(N))


if __name__ == '__main__':
    main()

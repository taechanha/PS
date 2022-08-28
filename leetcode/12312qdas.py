
def solution(n):
    cnt = 0
    for k in range(1, n):
        cnt += poll(n, k)
    return cnt


def poll(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    memo = {}
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j == 1:
                memo[(i, j)] = 1
            else:
                memo[(i, j)] = memo[(i - 1, j)] + memo[(i - 1, j - 1)]
    return memo[(n, k)]


res = solution(10)
print(res)

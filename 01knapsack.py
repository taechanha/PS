def KS(n, k):
    global X, weights, values

    if n == 0 or k == 0:
        return 0
    if X[n-1][k] != -1:
        return X[n-1][k]

    if weights[n-1] > k:
        X[n-1][k] = KS(n-1, k)
        return X[n-1][k]

    X[n-1][k] = max(KS(n-1, k), KS(n-1, k-weights[n-1]) + values[n-1])
    return X[n-1][k]


def solution(values, weights, k):
    global X
    N = len(values)
    X = [[-1] * (k+1) for _ in range(N)]

    # for row in X:
    # print(row)

    answer = KS(N, k)

    for row in X:
        print(row)
    return answer


values = [2, 2, 4, 3]
weights = [1, 3, 4, 2]
k = 5
res = solution(values, weights, k)

print(res)

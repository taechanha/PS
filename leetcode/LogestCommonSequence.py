def LCS(i, j, s, t, n, m, X):
    if i == n or j == m:
        return 0

    if X[i][j] != -1:
        return X[i][j]

    if s[i] == t[j]:
        X[i][j] = LCS(i+1, j+1, s, t, n, m, X) + 1
        return X[i][j]

    X[i][j] = max(LCS(i+1, j, s, t, n, m, X), LCS(i, j+1, s, t, n, m, X))
    return X[i][j]


def solution(s, t):
    n, m = len(s), len(t)
    X = [[-1] * m for _ in range(n)]
    return LCS(0, 0, s, t, n, m, X)


T = int(input())
for i in range(1, T+1):
    s, t = input().split()
    answer = solution(s, t)
    print(f"#{i} {answer}")

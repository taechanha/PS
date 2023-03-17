# 길이 N의 수열 A
# 길이 M의 수열 B가 있음
# 두 수열의 각 임의의 수 끼리 매칭을 만들어줌 (선으로 이음)
# 단, 선끼리 꼬이면 안 됨
# W는 주어짐
# W[1][2]와 같이 1과 2가 매칭됐을 때의 점수를 얻을 수 있음
#
# 어떻게 매칭을 해야 총 점수가 최대가 될 수 있는지
# N, M <= 1,000
# X <= 16

# 접근
# 전체 N, M을 모두 한 번에 고려하면 어렵다
# A의 i까지, B의 j까지만 먼저 고려해 작은 문제부터 풀어보자

# A: 1, 3, 2
# B: 2, 3, 1

# 그랬을 때, X[a][b] := A의 a까지, B의 b까지의 최대 점수로 정의한다


def solution(w, a, b):
    X = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            case1 = w[a[i]][b[j]]
            case2 = case3 = 0
            if i > 0 and j > 0:
                case1 += X[i-1][j-1]
            if j > 0:
                case2 = X[i][j-1]
            if i > 0:
                case3 = X[i-1][j]
            X[i][j] = max(case1, case2, case3)
            
    return X[n-1][m-1]


# @lru_cache(None)
# def X(i, j):  # i, j 부터 최대값
#     if i >= n or j >= m:
#         return 0
#     case1 = X(i+1, j+1) + w[a[i]-1][b[j]-1]
#     case2 = X(i, j+1)
#     case3 = X(i+1, j)
#     return max(case1, case2, case3)


n, m, c = map(int, input().split())
w = [list(map(int, input().split())) for _ in range(c)]
a, b = list(map(lambda x: int(x)-1, input().split())
            ), list(map(lambda x: int(x)-1, input().split()))
ans = solution(w, a, b)
print(ans)

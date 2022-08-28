def maxValueAtIndexK(N, K, M):

    # Stores the sum of elements
    # in the left and right of index K
    S1 = 0
    S2 = 0
    S1 = K * (K + 1) // 2
    S2 = (N - K - 1) * (N - K) // 2

    # Stores the maximum
    # possible value at index K
    X = (M + S1 + S2) // N

    # Prthe answer
    print(X)


# Driver Code
if __name__ == '__main__':

    # Given N, K & M
    N = 3
    K = 1
    M = 7
    maxValueAtIndexK(N, K, M)

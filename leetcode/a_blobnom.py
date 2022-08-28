def solution(A):
    A.sort()
    max_height = 0
    for i in range(len(A)):
        if i == 0 or i == len(A) - 1:
            continue
        if A[i-1] < A[i] and A[i] < A[i+1]:
            max_height = max(max_height, A[i] + A[i-1] + A[i+1])
    return max_height


n = int(input())
arr = list(map(int, input().split()))
print(solution(arr))

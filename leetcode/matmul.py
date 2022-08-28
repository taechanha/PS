def solution(arr1, arr2):
    a = len(arr1)
    b = len(arr2[0])
    answer = [[0 for col in range(b)] for row in range(a)]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

def max_path_sum(triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    if not triangle:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(max_path_sum(arr))

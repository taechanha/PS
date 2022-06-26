n, m = map(int, input().split())
lectures = list(map(int, input().split()))


def D(L):
    global lectures, n, m
    num_partition, sum = 1, 0
    for i in range(n):
        if sum + lectures[i] <= L:
            sum += lectures[i]
        else:
            num_partition += 1
            sum = lectures[i]
    return num_partition <= m


l = max(lectures)
r = pow(10, 9)
while l <= r:
    mid = (l + r) // 2
    if D(mid):  # mid보다 큰 케이스들은 모두 블루레이 m개로 분할 가능 -> mid보다 더 작은 케이스를 보자
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)

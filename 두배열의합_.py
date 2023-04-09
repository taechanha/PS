from bisect import bisect_left as bl, bisect_right as br

def partial_sum(arr, n) -> list[list]:
    return [[sum(arr[i:j+1]) for j in range(i, n)] for i in range(n)]

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))
cnt = 0

sum_a = partial_sum(A, n)
sum_b = partial_sum(B, m)
sum_b = sorted([sum_b[i][j] for i in range(m) for j in range(m-i)])

for i in range(n):
    nn = len(sum_a[i])
    for j in range(nn):
        target = T-sum_a[i][j]
        cnt += br(sum_b, target) - bl(sum_b, target)

print(cnt)
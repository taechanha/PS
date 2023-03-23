# 목표로 하는 숫자 x가 있음, n개의 수가 있음

# n <= 20
# x <= 1000

# n개의 수
# 200 60 30 50 100
# X = 140

# 최대 3개의 수를 골라 더해서 x 이상의 수 중 최솟값을 만들고 싶음
# 불가능하면 -1

from itertools import combinations as C


def solution(arr, x):
    n = len(arr)
    ans = float('inf')

    for i in range(1, 4):
        lst = list(sum(each) for each in list(C(arr, i)))  # nCr
        ans = min(ans, min(e for e in lst if e >= x))

    return -1 if ans == float('inf') else ans


x = 140
arr = [200, 60, 30, 50, 100]
ans = solution(arr, x)
print(ans)

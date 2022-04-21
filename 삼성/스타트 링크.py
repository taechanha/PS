# 1. 능력치 계산: (1, 2, 3) -> s[1][2], s[2][1], s[1][3], s[3][1], s[2][3], s[3][2] 계산하는 함수
# 2. nCr 계산
from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')
arr = list(range(n))
arr_half = len(arr) // 2
combs = list(combinations(arr, arr_half))
combs_half = len(combs) // 2

def get_abilities(arr):
    global s
    # (1, 2, 3) -> (1, 2), (1, 3), (2, 3) & the opposites also
    # abilities = 0
    # for i, idx in enumerate(arr):
    #     for jdx in arr[i+1:]:
    #         abilities += s[idx][jdx] + s[jdx][idx]
    # return abilities

    return sum( [ sum([s[idx][jdx] + s[jdx][idx] for jdx in arr[i+1:] ]) for i, idx in enumerate(arr) ] )


for c1, c2 in zip(combs[:combs_half], reversed(combs[combs_half:])):
    # (1,2,3) (4,5,6)
    diff = abs(get_abilities(c1) - get_abilities(c2))
    min_diff = min(min_diff, diff)

print(min_diff)

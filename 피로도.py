# 2:30 ~ 2:43
from itertools import permutations as P

def solution(k, dungeons):
    max_cnt = -1
    for cases in P(dungeons):
        temp_k = k
        cnt = 0
        for require, consume in cases:
            if temp_k < require:
                continue
            if temp_k < consume:
                continue
            temp_k -= consume
            cnt += 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
res = solution(k, dungeons)
print(res)

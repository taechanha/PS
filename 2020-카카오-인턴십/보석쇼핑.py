
# # O(N^2)
# def solution(gems):
#     kinds = len(set(gems))
#     n = len(gems)
#     range_list = []
#     for i in range(n):
#         temp_set = set()
#         for j in range(i, n):
#             temp_set.add(gems[j])
#             if len(temp_set) == kinds:
#                 range_list.append([i, j])
#                 break
#     min_range = float('inf')
#     ans = []
#     for s, e in range_list:
#         if min_range > e - s:
#             min_range = e - s
#             ans = [s+1, e+1]
#     return ans

# O(n)
# 투 포인터 + 맵
from collections import defaultdict


def solution(gems):
    gdict = defaultdict(int)
    gnum = len(set(gems))

    left = 0
    right = 0
    range_list = []
    while right < len(gems):
        gdict[gems[right]] += 1
        right += 1

        if len(gdict) == gnum:
            while left < right:
                if gdict[gems[left]] <= 1:
                    break
                gdict[gems[left]] -= 1
                left += 1

            range_list.append([left, right])
    
    min_range = float('inf')
    ans = []
    for s, e in range_list:
        if min_range > e - s:
            min_range = e - s
            ans = [s+1, e] # e는 +1 해주지 않는 이유: right += 1 해주면서 항상 한 칸 더 앞서나가있음
    return ans

    # left, right = 0에서 시작
    # right가 끝에 다다를 때 까지 반복
    # - right 위치 요소 set에 추가하고 ++
    # - 검사 - set이 set(kinds)와 같은지 -> 같다면 min range 추가, bag에서 left 요소 삭제, left += 1
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
res = solution(gems)
print(res)

from itertools import product as P
from collections import defaultdict


def is_matched(origin, hidden):
    # mustbe same(length of both)
    if len(origin) != len(hidden):
        return False

    for oc, hc in zip(origin, hidden):
        if hc == '*':
            continue
        if oc != hc:
            return False
    return True

# def solution(user_id, banned_id):
#     answer = 0
#     lu = len(user_id)
#     lb = len(banned_id)
#     i = 0 # user
#     j = 0 # banned
#     check = 0

#     user_id = user_id[:check] + user_id[check + 1:] # control search space
#     print(user_id)
#     check = -1
#     while i < lu and j < lb:
#         # why i < lu? -> condition of "not counting"
#         if is_matched(user_id[i], banned_id[j]):
#             if check == -1: # 단 한 번만 수행
#                 check = i
#             i += 1
#             j += 1
#         else:
#             i += 1

#     if j == lb:
#         answer += 1

#     return answer


# u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# b = ["fr*d*", "abc1**"]
# u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# b = ["*rodo", "*rodo", "******"]
u = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

b = ["fr*d*", "*rodo", "******", "******"]

# frodo crodo abc123 frodoc
# fradi frodo abc123 frodoc
# fradi crodo abc123 frodoc

# b = list(set(b))
# print(b)
res = list(P(u, b))
# print(res)
# d = defaultdict(int)
poplist = []
for i, each in enumerate(res):
    user = each[0]
    ban = each[1]
    if not is_matched(user, ban):
        poplist.append(i)
for idx in poplist[::-1]:
    res.pop(idx)

print(res)
#         d[b] += 1

# print(d)

# print(solution(u, b))


# # [1]
# # 하이레벨 풀이 절차
# # banned_id를 기준으로,
# # 1. banned_id의 첫번째 *rodo에 대해서, user_id를 하나하나 탐색하며 매칭되는 것이 있는지 보고, 있다면 걔를 제외하고
# # 2. banned_id의 두번째 *rodo에 대해서, 매칭된 것을 제외한 나머지 user_id에서 매칭되는 것이 있나 보고, 마찬가지로 제외하고,
# # 3. 1 - 2반복 언제까지? banned_id 다 매칭될 때까지


# # frodo -> [fradi, crodo, ...], crodo  =>  (frodo, crodo)
# # fradi -> [frodo, crodo, ...], frodo  =>  (fradi, frodo)
# # fradi -> [frodo, crodo, ...], crodo  =>  (fradi, crodo)


# # [2]
# # "매칭" 구현
# # fro*d* => frodo

class Candidate:
    def __init__(self, lang, job, level, food, score) -> None:
        self.language = lang
        self.job = job
        self.level = level
        self.food = food
        self.score: int = score


def store_info(info):
    candidates = []
    for candidate in info:
        lang, job, level, food, score = candidate.split()
        candidates.append(Candidate(lang, job, level, food, int(score)))
    return candidates


def solution(info, query):
    ans = []
    # 어딘가에 저장이 되어 있어야함. 매번 계산하고 처리하면 효율성 떨어질 것
    # 1. info 저장
    candidates = store_info(info)
    # 2. query 수행
    #   a b c d e f g h i
    for q in query:
        lang, _, job, _, level, _, food, score = q.split()
        filtered = filter_cand(candidates, 'lang', lang)
        filtered = filter_cand(filtered, 'job', job)
        filtered = filter_cand(filtered, 'level', level)
        filtered = filter_cand(filtered, 'food', food)
        filtered = filter_cand(filtered, 'score', int(score))
        ans.append(len(filtered))

    return ans


def filter_cand(candidates, by: str, val):
    filtered = []
    if val == '-':
        return candidates
    if by == 'score':
        return [x for x in candidates if x.score >= val]
    elif by == 'lang':
        return [x for x in candidates if x.language == val]
    elif by == 'job':
        return [x for x in candidates if x.job == val]
    elif by == 'level':
        return [x for x in candidates if x.level == val]
    elif by == 'food':
        return [x for x in candidates if x.food == val]
    return filtered


# * [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
res = solution(info, query)
print(res)

#########################################################################
#########################################################################
#########################################################################
################## ACCEPTED code - efficiency ###########################
#########################################################################
#########################################################################
#########################################################################

# from collections import defaultdict
# import bisect


# def solution(info, query):
#     # javabackendjuniorpizza150, ----, cpp-senior-pizza1
#     lex = defaultdict(list)
#     for lang in ["cpp", "java", "python", "-"]:
#         for job in ["backend", "frontend", "-"]:
#             for level in ["junior", "senior", "-"]:
#                 for food in ["chicken", "pizza", "-"]:
#                     lex[lang+job+level+food] = []

#     for candidate in info:
#         lang, job, level, food, score = candidate.split()
#         # print(lang, job, level, food, score)
#         for a in [lang, '-']:
#             for b in [job, '-']:
#                 for c in [level, '-']:
#                     for d in [food, '-']:
#                         lex[a+b+c+d].append(int(score))
#         # print(lex[lang+job+level+food])

#     for key in lex.keys():
#         lex[key].sort()

#     ans = []
#     for q in query:
#         lang, _, job, _, level, _, food, score = q.split()
#         key = lang+job+level+food
#         idx = bisect.bisect_left(lex[key], int(score))
#         ans.append(len(lex[key]) - idx)
#         # idx = bsearch(lex[key], int(score))
#         # ans.append(len(lex[key][:idx]))

#         # ans.append(
#         #     sum([1 for cand_score in lex[key] if cand_score >= int(score)]))
#     return ans
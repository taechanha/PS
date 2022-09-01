# 4:03 ~ 4:12

# from itertools import permutations as P

# a, b = map(int, input().split())

# max_a = -1
# for each in P(str(a)):
#     a = int(''.join(each))
#     if len(str(a)) != len(each):
#         continue
#     a = int(a)
#     if a < b:
#         max_a = max(max_a, a)

# print(max_a)

things = '1234'
n = len(things)
visited = [False] * n
data = []


# def permutation(things, chosen):
#     if len(chosen) == 4:
#         data.append(chosen)
#         return
#     for i in range(n):
#         if visited[i]:
#             continue
#         chosen += things[i]
#         visited[i] = True
#         permutation(things, chosen)
#         visited[i] = False
#         chosen = chosen[:-1]


# permutation(things, "")
# print(data)

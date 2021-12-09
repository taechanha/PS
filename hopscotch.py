def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[-1])


# [1,2,3,5] : 1
# [5,6,7,8] : 2
# [4,3,2,1] : 3

# [10,11,12,11] : 2

# [16,15,11,13] : 3

print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))


# def solution(land):
#     chosen = []
#     if len(land) == 1:
#         return max(land)
#     return helper(land, -1, 0, chosen)

# def helper(land, idx_i, idx_j, chosen):
#     # base case
#     if len(chosen) == len(land):
#         return sum(chosen)
#     else:
#         curr_max = 0
#         for i in range(len(land[0])):
#             for j in range(idx_j, len(land)):
#                 if i == idx_i: continue

#                 chosen.append(land[j][i])

#                 curr = helper(land, i, j+1, chosen)
#                 if curr > curr_max:
#                     curr_max = curr

#                 chosen.pop()

#         return curr_max

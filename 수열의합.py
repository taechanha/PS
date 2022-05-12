# # 1. sum(some_list) == n
# # 2. len(some_list) >= l
# # 3. some_list: shortest length, not negative numbers
# # 4. some_list: consecutive


# # "가장 짧은"을 어떻게 보장하지?
# # 주어진 수에 가장 가까운 수부터 역순으로 탐색하면 될까?

# def dfs(num: int, chosen: list):
#     # if sum(chosen) > n:
#     #     return

#     if sum(chosen) == n and len(chosen) >= l:
#         print(chosen)
#         exit()
#     else:
#         for i in range(num, 0, -1):
#             # choose
#             chosen.append(i)
#             # explore
#             dfs(i - 1, chosen)
#             # unchoose
#             chosen.pop()


# def prefix_sum(n):
#     temp = list(range(n))
#     prefix = [0] * n
#     for i in range(1, n):
#         prefix[i] = prefix[i - 1] + temp[i]
#     return prefix


# def range_sum(prefix, s, e):
#     if s <= 0:
#         s = 1
#     return prefix[e] - prefix[s - 1]


# n, l = map(int, input().split())
# prefix = prefix_sum(n)

# for new_len in range(l, n + l - 1):
#     for j in range(n - new_len + 1):
#         # print(len(prefix), range(j, j + new_len - 1), end=' ')
#         # print(range_sum(prefix, j, j + new_len - 1))
#         res = range_sum(prefix, j, j + new_len - 1)
#         if res > n:
#             break
#         elif res == n:
#             print(*range(j, j + new_len))
#             exit()

# print(-1)

# # 10000 2
# # 100000 2
# # 1000000 2
# # 10000000 2
# # 100000000 2
# # 1000000000 2


# # for i in range(n, -1, -1):
# #     chosen = []
# #     for j in range(i, -1, -1):
# #         chosen.append(j)

# #         if sum(chosen) > n:
# #             break
# #         elif sum(chosen) == n:
# #             if j == 1:
# #                 chosen.append(0)
# #             if len(chosen) >= l:
# #                 print(*sorted(chosen))
# #                 exit()
# #             else:
# #                 break
# #     # print(i, j, chosen)
# # print(-1)


# # n == 3
# # l == 2
# # answer = [1, 2]

# # 1.
# #     i = 3, chosen = [3]
# #     i = 2, chosen = [3, 2]
# #     -> ret ( len, sum )

# # 2.
# #     i = 2, chosen = [2]
# #     i = 1, chosen = [2, 1]


n, l = map(int, input().split())
s = 0
x = -1
checkpoint = 0

# following mentioned prob statement
for i in range(l, 101):
    s = (pow(i, 2) - i) / 2  # Summation
    if (n - s) % i == 0 and (n - s) // i >= 0:  # validation; x being integer and not negative
        x = int((n - s) // i)
        checkpoint = i
        break

# print as ps
if x == -1:
    print(-1)
else:
    # Ex. 5 6 7, when x equals 5, checkpoint 3
    print(*[x + i for i in range(checkpoint)])

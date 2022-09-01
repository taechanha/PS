# # 4:43 ~
# def get_abs_time(t):
#     h, m = t.split(':')
#     return int(h) * 60 + int(m)


# def get_rel_time(t):
#     a, b = divmod(t, 60)
#     if a // 10 == 0:
#         a = '0' + str(a)
#     if b // 10 == 0:
#         b = '0' + str(b)
#     return f"{a}:{b}"


# n = int(input())
# t1_acc, t2_acc = 0, 0
# t1 = t2 = 0
# t1w = t2w = 0
# changed = False
# base = get_abs_time('48:00')
# for _ in range(n):
#     team, time = input().split()
#     abs_time = get_abs_time(time)

#     if team == '1':
#         recent_t1 = abs_time
#         t1w += 1
#         # 팀2가 이기고 있었던 경우
#         if t1w == t2w:
#             t2_acc += abs_time - recent_t2  # (48:00 - 01:10) - 21:10
#         elif t1w > t2w:
#             t1 = base - abs_time
#     else:
#         recent_t2 = abs_time
#         t2w += 1
#         if t1w == t2w:
#             t1_acc += abs_time - recent_t1
#         elif t2w > t1w:
#             t2 = base - abs_time

#     print("\n", get_rel_time(t1), get_rel_time(t2),
#           get_rel_time(t1_acc), get_rel_time(t2_acc))

# print(team, time, ret, res, base)
# 3
# 1 01:10
# 2 21:10
# 2 31:30


# 5:20 ~

# dict of dict
# {
#     1: {
#         'n_submit' = 0,
#         'submit_time' = 0,
#         'submits': {
#             1: 0,
#             2: 0,
#         }
#     },
#     2: {},
# }

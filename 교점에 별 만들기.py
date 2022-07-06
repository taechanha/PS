# 3:02 ~ 4:42
# re-try

def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False

# L1 = line([0, 1], [2, 3])
# L2 = line([2, 3], [0, 4])

# R = intersection(L1, L2)
# if R:
#     print("Intersection detected:", R)
# else:
#     print("No single intersection point detected")


def solution(line):
    n = len(line)
    intersection_points = []
    min_x = min_y = float('inf')
    max_x = max_y = -float('inf')
    # 1. 교점 구하기
    for i in range(n):
        for j in range(i+1, n):
            L1, L2 = tuple(line[i]), tuple(line[j])
            ret = intersection(L1, L2)
            if ret == False:
                continue
            if is_integer(ret):
                x, y = int(ret[0]), -int(ret[1])
                intersection_points.append((x, y))
                min_x, max_x = min(min_x, x), max(max_x, x)
                min_y, max_y = min(min_y, y), max(max_y, y)
    # print(min_x, max_x, min_y, max_y)
    board = [['.'] * (abs(min_x)+abs(max_x)+1)
             for _ in range(abs(min_y)+abs(max_y)+1)]
    # print("max and min", min_x, min_y, max_x, max_y)
    # 2. 좌표대로 별 찍기
    for x, y in intersection_points:
        # x += abs(min_x)
        # y -= abs(min_y)
        board[max_y-y][x-min_x] = '*'

    nn = len(board)
    for start in range(nn):
        if '*' in board[start]:
            break
    for end, i in enumerate(range(nn-1, -1, -1)):
        if '*' in board[i]:
            break

    ans = []
    for i in range(start, (nn-end)):
        new_row = ''.join(board[i])
        ans.append(new_row)
    return ans


def is_integer(ret):
    n1, n2 = ret
    for n in n1, n2:
        n = str(n)
        i = n.index('.')
        new = n[i+1:]
        if len(new) != 1:
            return False
        if new[0] != '0':
            return False
    return True


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
# line = [[1, -1, 0], [2, -1, 0]]
# line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
res = solution(line)
print(res)


# (-1, 1), (1, 1) -> (0, 0), (2, 0)
# ["....*....", (0, 4) -> [0][4]
#  ".........",
#  ".........",
#  "*.......*", (-4, 1) (4, 1) -> [4][0], [4][8]
#  ".........",
#  ".........",
#  ".........",
#  ".........",
#  "*.......*"] (-4, -4), (4, -4) -> [7][0], [7][7]

# (4, 1), (4, -4), (-4, -4), (-4, 1), (0, 4)입니다.

# 다시
from collections import defaultdict


def bfs_snail(board, r, c):
    q = [(r, c)]
    dist = dict()
    dist[(r, c)] = 0
    while q:
        r, c = q.pop(0)
        if board[r][c] != 0:
            board[r][c] = 0
            return dist[(r, c)], r, c

        # 1, 2, 3, 4: 위 오른, 왼, 아래
        for dir in range(1, 5):
            nr, nc, msg = ctrl_move(board, dir, r, c)
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if (nr, nc) in dist:
                continue
            if msg == 'moved':
                q.append((nr, nc))
                dist[(nr, nc)] = dist[(r, c)] + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if (nr, nc) in dist:
                continue
            q.append((nr, nc))
            dist[(nr, nc)] = dist[(r, c)] + 1

# ret: r, c


def find_end_and_update_dict(r, c, start_end_dict):
    delete_list = []
    for k, v in start_end_dict.items():
        for target_r, target_c in v:
            if (r, c) == (target_r, target_c):
                start_end_dict[k].remove((r, c))
                ret = start_end_dict[k][0]
                delete_list.append(k)
                break

    for key in delete_list:
        del start_end_dict[key]
    try:
        return ret
    except:
        print((r, c), start_end_dict[k])

# ret: dist[(r, c)], r, c


def ctrl_move(board, dir, r, c):
    flag = 0
    if dir == 1:
        while r > 0:
            r -= 1
            flag = 1
            if board[r][c] != 0:
                return r, c, 'moved'
        if flag == 1:
            return r, c, 'moved'
        else:
            return r, c, 'not_moved'
    elif dir == 2:
        while c < 3:
            c += 1
            flag = 1
            if board[r][c] != 0:
                return r, c, 'moved'
        if flag == 1:
            return r, c, 'moved'
        else:
            return r, c, 'not_moved'
    elif dir == 3:
        while c > 0:
            c -= 1
            flag = 1
            if board[r][c] != 0:
                return r, c, 'moved'
        if flag == 1:
            return r, c, 'moved'
        else:
            return r, c, 'not_moved'
    elif dir == 4:
        while r < 3:
            r += 1
            flag = 1
            if board[r][c] != 0:
                return r, c, 'moved'
        if flag == 1:
            return r, c, 'moved'
        else:
            return r, c, 'not_moved'


def bfs(board, r, c, end_r, end_c):
    """
    ret: dist, r, c
    """
    init_r, init_c = r, c
    q = [(r, c)]
    dist = dict()
    dist[(r, c)] = 0
    while q:
        r, c = q.pop(0)
        if (r, c) == (end_r, end_c):
            board[init_r][init_c] = 0
            board[r][c] = 0
            return dist[(r, c)], r, c

        # 1, 2, 3, 4: 위 오른, 왼, 아래
        for dir in range(1, 5):
            nr, nc, msg = ctrl_move(board, dir, r, c)
            # debug
            # if (init_r, init_c) == (3, 0):
            #     print(nr, nc)
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if (nr, nc) in dist:
                continue
            if msg == 'moved':
                q.append((nr, nc))
                dist[(nr, nc)] = dist[(r, c)] + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if (nr, nc) in dist:
                continue
            q.append((nr, nc))
            dist[(nr, nc)] = dist[(r, c)] + 1


def solution(board, r, c):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # (시작점, 끝점)을 갖는 리스트
    start_end_dict = defaultdict(list)
    dict_key_len = len(start_end_dict.keys())
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                start_end_dict[board[i][j]].append((i, j))
    # Ex. {1: [(i, j), (k, l)]}

    # 리스트 크기만큼 루프 돌면서 bfs
    ans = 0
    # card마다 탐색 수행
    for i, _ in enumerate(range(len(start_end_dict.keys()))):
        if board[r][c] != 0:
            end_r, end_c = find_end_and_update_dict(r, c, start_end_dict)
            dist, r, c = bfs(board, r, c, end_r, end_c)
        else:
            flag = 0
            ret = bfs_snail(board, r, c)
            dist, r, c = ret
            # if ret != None:
            #     dist, r, c = ret
            # else:
            #     for R in range(4):
            #         for C in range(4):
            #             ret = bfs_snail(board, R, C)
            #             if ret != None:
            #                 dist, r, c = ret
            #                 flag = 1
            #                 break
            #         if flag == 1:
            #             break
            #
            end_r, end_c = find_end_and_update_dict(r, c, start_end_dict)
            try:
                dist2, r, c = bfs(board, r, c, end_r, end_c)
            except:
                print("DEBUG: ", bfs(board, r, c, end_r, end_c))
                print(board)
                print("current (r, c): ", (r, c))
                print("destina (r, c): ", (end_r, end_c))
            dist += dist2

            # DEBUG
            # if i == 1:
            # print((r, c), dist)
            # exit()

        ans += dist

        # 한 스텝 진행할 때 마다 +2 (엔터키)
        ans += 2
        # print("step: ", i+1, "키 조작: ", ans)
    return ans


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
# r = 1
# c = 0
board = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]
r = 0
c = 1
res = solution(board, r, c)
print(res)


# Enter
# ctrl + 상하좌우
# 상하좌우

# 누가봐도 완전탐색 - 탐색 범위가 작아서 전체 돌려도 무방
# 최소는 어떻게 구할까?

def find_nearest_card_linear(dir, r, c):
    if dir == 1:
        while r > 0:
            r -= 1
            if board[r][c] != 0:
                return r, c, 'moved'
    elif dir == 2:
        while c < 3:
            c += 1
            if board[r][c] != 0:
                return r, c, 'moved'
    elif dir == 3:
        while c > 0:
            c -= 1
            if board[r][c] != 0:
                return r, c, 'moved'
    elif dir == 4:
        while r < 3:
            r += 1
            flag = 1
            if board[r][c] != 0:
                return r, c, 'moved'


def find_nearest_card(r, c):
    """ 
    if meet non - zero value, 
    return dist, r, c 
    """
    q = [(r, c)]
    dist = dict()
    dist[(r, c)] = 0

    while q:
        r, c = q.pop(0)
        if board[r][c] != 0:
            return dist[(r, c)], r, c
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < 4 and 0 <= nc < 4):
                continue
            if (nr, nc) in dist:
                continue
            q.append((nr, nc))
            dist[(nr, nc)] = dist[(r, c)] + 1


def is_in_boundary(r, c):
    return 0 <= r < n and 0 <= c < n


def update_num_adj(rc_list):
    max_cell = []
    max_num = -1

    for r, c in rc_list:
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not is_in_boundary(nr, nc):
                continue
            if occupied[nr][nc]:
                continue
            num_adj[r][c] += 1

        if num_adj[r][c] >= max_num:
            max_num = num_adj[r][c]
            max_cell.append((r, c, max_num))

    return max_nums(max_cell, max_num)


def update_num_adj_like(liking_list):
    max_cell = []
    max_num = -1
    for i in range(n):
        for j in range(n):
            if occupied[i][j]:
                continue
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if not is_in_boundary(nr, nc):
                    continue
                # print(nr, nc, i, j, board, board[nr][nc], liking_list)
                if board[nr][nc] in liking_list:
                    num_adj_like[i][j] += 1

            if num_adj_like[i][j] >= max_num:
                max_num = num_adj_like[i][j]
                max_cell.append((i, j, max_num))
    # print(num_adj_like)
    return max_nums(max_cell, max_num)


def max_nums(max_cell, max_num):
    ret = []
    for i, j, each_max_num in max_cell:
        if max_num == each_max_num:
            ret.append((i, j))
    return ret


def utility():
    sum_count = 0
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if not is_in_boundary(nr, nc):
                    continue
                if board[i][j] == False:
                    continue
                if board[nr][nc] in std_2_liking_std[board[i][j]]:
                    count += 1
            if count == 2:
                count = 10
            elif count == 3:
                count = 100
            elif count == 4:
                count = 1000
            sum_count += count
    return sum_count


n = int(input())
board = [[False for _ in range(n)] for __ in range(n)]
occupied = [[False for _ in range(n)] for __ in range(n)]
std_2_liking_std = {}
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(pow(n, 2)):
    num_adj = [[0 for _ in range(n)] for __ in range(n)]
    num_adj_like = [[0 for _ in range(n)] for __ in range(n)]
    target, a, b, c, d = map(int, input().split())
    std_2_liking_std[target] = [a, b, c, d]

    cells_adj_like = update_num_adj_like([a, b, c, d])

    if len(cells_adj_like) > 1:
        cells_adj = update_num_adj(cells_adj_like)
        cells_adj.sort(key=lambda x: (x[0], x[1]))
        r, c = cells_adj[0]

        occupied[r][c] = True
        board[r][c] = target

    else:
        cells_adj_like.sort(key=lambda x: (x[0], x[1]))
        r, c = cells_adj_like[0]
        occupied[r][c] = True
        board[r][c] = target

    # if target == 1:
    #     print()
    #     print(cells_adj_like)
    #     print(cells_adj)
    #     print(r, c)

# print(board)
print(utility())

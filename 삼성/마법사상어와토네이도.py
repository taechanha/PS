# def tornado(n):
#     global board
#     # 3x3 케이스 테스트
#     r, c = n//2, n//2
#     count = 1
#     even = 0
#     i = 0
#     flag = 0
#     while flag == 0:
#         if even != 0 and even % 2 == 0:
#             count += 1
#         if count == n:
#             count -= 1
#             flag = 1
#         nr = r + (dr[i % 4] * count)
#         nc = c + (dc[i % 4] * count)

#         # 모래 흩날리기
#         temp_board = [row[:] for row in board]
#         curr_dir = get_dir(r, c, nr, nc)
#         if curr_dir == 'up':
#             for _ in range(3):
#                 temp_board = rotate_90_cw(temp_board)
#             sandstorm(r, c, nr, nc, temp_board)  # 왼쪽 가정
#             temp_board = rotate_90_cw(temp_board)
#         elif curr_dir == 'right':
#             for _ in range(2):
#                 temp_board = rotate_90_cw(temp_board)
#             sandstorm(r, c, nr, nc, temp_board)  # 왼쪽 가정
#             for _ in range(2):
#                 temp_board = rotate_90_cw(temp_board)
#         elif curr_dir == 'down':
#             temp_board = rotate_90_cw(temp_board)
#             sandstorm(r, c, nr, nc, temp_board)  # 왼쪽 가정
#             for _ in range(3):
#                 temp_board = rotate_90_cw(temp_board)
#         else:
#             sandstorm(r, c, nr, nc, temp_board)  # 왼쪽 가정

#         board = [row[:] for row in temp_board]

#         r = nr
#         c = nc

#         even += 1
#         i += 1

#         # print(r, c)
#         # exit()


# def out_of_bound(r, c):
#     return not (0 <= r < n and 0 <= c < n)


# def sandstorm(r, c, nr, nc, temp_board):
#     global ans
#     rest = temp_board[nr][nc]
#     # 왼쪽 가정
#     for dr, dc, percent in [(-1, 0, 1), (1, 0, 1), (-1, -1, 7), (1, -1, 7),
#                             (-2, -1, 2), (2, -1, 2), (-1, -2, 10),
#                             (1, -2, 10), (0, -3, 5)]:
#         applied_r = r + dr
#         applied_c = c + dc

#         qty = int(temp_board[nr][nc] * (percent / 100))
#         rest = rest - qty
#         if out_of_bound(applied_r, applied_c):
#             ans += qty
#         else:
#             temp_board[applied_r][applied_c] += qty
#     temp_board[r][c-2] = rest
#     temp_board[nr][nc] = 0


# def rotate_90_cw(board):
#     n = len(board)
#     temp = [[0] * n for _ in range(n)]
#     for r in range(n):
#         for c in range(n):
#             temp[c][n-1-r] = board[r][c]
#     return temp


# def get_dir(r, c, nr, nc):
#     # a b a+1, b -> down
#     if nr == r + 1:
#         return 'down'
#     # a b a-1, b -> up
#     elif nr == r - 1:
#         return 'up'
#     # a b a, b+1 -> right
#     elif nc == c + 1:
#         return 'right'
#     # a b a, b-1 -> left
#     elif nc == c - 1:
#         return 'left'

# 좌하우상
# dr = [0, 1, 0, -1]
# dc = [-1, 0, 1, 0]
# tornado(n)

def out_of_bound(r, c):
    return not (0 <= r < n and 0 <= c < n)


def sandstorm(times, delta_r, delta_c, dir):
    global ans, s_r, s_c

    for _ in range(times):
        s_r += delta_r
        s_c += delta_c
        if s_c < 0:
            break

        accum = 0
        for dr, dc, pct in dir:
            nr = s_r + dr
            nc = s_c + dc

            if pct == 0:
                qty = board[s_r][s_c] - accum
            else:
                qty = int(board[s_r][s_c] * pct)
                accum += qty

            if out_of_bound(nr, nc):
                ans += qty
            else:
                board[nr][nc] += qty


global board, ans
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

ans = 0
s_r, s_c = n//2, n//2

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(r, -c, z) for r, c, z in left]
down = [(-c, r, z) for r, c, z in left]
up = [(c, r, z) for r, c, z in left]

# 좌하 우상
for times in range(1, n+1):
    if times % 2:
        sandstorm(times, 0, -1, left)
        sandstorm(times, 1, 0, down)
    else:
        sandstorm(times, 0, 1, right)
        sandstorm(times, -1, 0, up)

print(ans)

# def recount(time, dx, dy, direction):
#     global ans, s_x, s_y

#     # y좌표 계산 & x좌표 갱신
#     for _ in range(time):
#         s_x += dx
#         s_y += dy
#         if s_y < 0:  # 범위 밖이면 stop
#             break

#         # 3. a, out_sand
#         total = 0  # a 구하기 위한 변수
#         for dx, dy, z in direction:
#             nx = s_x + dx
#             ny = s_y + dy
#             if z == 0:  # a(나머지)
#                 new_sand = sand[s_x][s_y] - total
#             else:  # 비율
#                 new_sand = int(sand[s_x][s_y] * z)
#                 total += new_sand

#             if 0 <= nx < N and 0 <= ny < N:   # 인덱스 범위이면 값 갱신
#                 sand[nx][ny] += new_sand
#             else:  # 범위 밖이면 ans 카운트
#                 ans += new_sand


# N = int(input())
# sand = [list(map(int, input().split())) for _ in range(N)]

# # 2. 방향별 모래 비율 위치
# left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
#          (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
# right = [(x, -y, z) for x, y, z in left]
# down = [(-y, x, z) for x, y, z in left]
# up = [(y, x, z) for x, y, z in left]

# s_x, s_y = N//2, N//2  # 시작좌표(x좌표)
# ans = 0  # out_sand

# # 1.토네이도 회전 방향(y위치)
# for i in range(1, N + 1):
#     if i % 2:
#         recount(i, 0, -1, left)
#         recount(i, 1, 0, down)
#     else:
#         recount(i, 0, 1, right)
#         recount(i, -1, 0, up)

# print(ans)

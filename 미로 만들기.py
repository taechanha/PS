# 6:02 ~


# LFFRFF

# ...
# .
# .

# LFLFRRFLFRRFLF


#.#
# ...
#.#

# (0, 1),
# (1, 0), (1, 1), (1, 2),
# (2, 1)

# 1. r의 최대, c의 최대를 기억
# 2. 이 정보로 #로 초기화된 max_r, max_c 크기의 board 생성
# 3. 이동한 좌표 순회하며 board 값 .로 변경

# 상우하좌
# 0123
right = {
    0: 1, 1: 2, 2: 3, 3: 0
}
left = {
    3: 2, 2: 1, 1: 0, 0: 3
}

n = int(input())
curr_dir = 2
curr_pos = (0, 0)
moved = [curr_pos]
for si in input():

    if si in ('R', 'L'):
        if si == 'R':
            curr_dir = right[curr_dir]
        else:
            curr_dir = left[curr_dir]
    else:
        if curr_dir == 0:  # 상
            curr_pos = (curr_pos[0]-1, curr_pos[1])
            moved.append(curr_pos)
        elif curr_dir == 2:  # 하
            curr_pos = (curr_pos[0]+1, curr_pos[1])
            moved.append(curr_pos)
        elif curr_dir == 1:  # 우
            curr_pos = (curr_pos[0], curr_pos[1]+1)
            moved.append(curr_pos)
        else:  # 좌
            curr_pos = (curr_pos[0], curr_pos[1]-1)
            moved.append(curr_pos)

max_r, max_c = 0, 0
min_r, min_c = 0, 0
for move in moved:
    r, c = move
    max_r, max_c = max(max_r, r), max(max_c, c)
    min_r, min_c = min(min_r, r), min(min_c, c)

max = max(max_r, max_c)
board = [['#'] * (max+1) for _ in range(max+1)]

for i, move in enumerate(moved):
    moved[i] = (move[0] - min_r, move[1] - min_c)
    r, c = move
    board[r][c] = '.'

print(moved, min_r, min_c, max_r, max_c, max)

for row in board:
    print(row)

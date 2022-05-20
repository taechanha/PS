# 9:20 ~ 9:46

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

# for for -> 삼면 이상(경계 포함)이 바다가 아닌 경우 temp에 X 추가 아니면 . 그대로
temp = [row[:] for row in board]
for r in range(R):
    for c in range(C):
        if board[r][c] == '.':
            continue
        assert board[r][c] == 'X'
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not(0 <= nr < R and 0 <= nc < C):
                cnt += 1
                continue
            if board[nr][nc] == '.':
                cnt += 1
        if cnt >= 3:
            temp[r][c] = '.'

# 행 탐색 -> X가 있는 행, 열만 ans에 담아 출력
board = [row[:] for row in temp]
rows = set()
cols = set()
temp = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'X':
            rows.add(r)
            temp.append(board[r])
            break

# for row in temp:
#     print(row)

board = [row[:] for row in temp]

for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c] == 'X':
            cols.add(c)

temp = []

assert set(sorted(cols)) == cols

# print(cols)

for r in range(len(board)):
    temp.append(board[r][min(cols): max(cols)+1])


for i in range(len(temp)):
    temp[i] = ''.join(temp[i])

for row in temp:
    print(row)

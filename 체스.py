# 2:25 ~ 3:11

knight_moves = [(-2, -1), (-1, -2), (-2, 1), (-1, 2),
                (1, 2), (2, 1), (2, -1), (1, -2)]
knight_positions = []
queen_positions = []
n, m = map(int, input().split())
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
board = [['-'] * m for _ in range(n)]

for i in range(1, (q[0]*2)+1, 2):
    r, c = q[i]-1, q[i+1]-1
    board[r][c] = 'q'
    queen_positions.append((r, c))

for i in range(1, (k[0]*2)+1, 2):
    r, c = k[i]-1, k[i+1]-1
    board[r][c] = 'k'
    knight_positions.append((r, c))

for i in range(1, (p[0]*2)+1, 2):
    r, c = p[i]-1, p[i+1]-1
    board[r][c] = 'p'

# logic
# knight
for r, c in knight_positions:
    for dr, dc in knight_moves:
        nr, nc = r+dr, c+dc
        if not (0 <= nr < n and 0 <= nc < m):
            continue
        board[nr][nc] = 'o'

# queen
for r, c in queen_positions:
    # 서  북  동  남
    for dc in range(1, m):
        nc = c-dc
        if not (0 <= nc < m and (board[r][nc] == '-' or board[r][nc] == 'o')):
            break
        board[r][nc] = 'o'

    for dr in range(1, n):
        nr = r-dr
        if not (0 <= nr < n and (board[nr][c] == '-' or board[nr][c] == 'o')):
            break
        board[nr][c] = 'o'
    for dc in range(1, m):
        nc = c+dc
        if not (0 <= nc < m and (board[r][nc] == '-' or board[r][nc] == 'o')):
            break
        board[r][nc] = 'o'
    for dr in range(1, n):
        nr = r+dr
        if not (0 <= nr < n and (board[nr][c] == '-' or board[nr][c] == 'o')):
            break
        board[nr][c] = 'o'

    # 북서 북동 남동 남서
    for d in range(1, max(n, m)):
        nr, nc = r-d, c-d
        if not (0 <= nr < n and 0 <= nc < m and (board[nr][nc] == '-' or board[nr][nc] == 'o')):
            break
        board[nr][nc] = 'o'
    for d in range(1, max(n, m)):
        nr, nc = r-d, c+d
        if not (0 <= nr < n and 0 <= nc < m and (board[nr][nc] == '-' or board[nr][nc] == 'o')):
            break
        board[nr][nc] = 'o'
    for d in range(1, max(n, m)):
        nr, nc = r+d, c-d
        if not (0 <= nr < n and 0 <= nc < m and (board[nr][nc] == '-' or board[nr][nc] == 'o')):
            break
        board[nr][nc] = 'o'
    for d in range(1, max(n, m)):
        nr, nc = r+d, c+d
        if not (0 <= nr < n and 0 <= nc < m and (board[nr][nc] == '-' or board[nr][nc] == 'o')):
            break
        board[nr][nc] = 'o'

# answer
cnt = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == '-':
            cnt += 1

# for row in board:
    # print(row)

print(cnt)

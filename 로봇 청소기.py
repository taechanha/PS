def bfs(r, c):
    Q = [(r, c)]
    dist = dict()
    dist[(r, c)] = 0
    while Q:
        r, c = Q.pop(0)
        if board[r][c] == '*':
            return dist[(r, c)], r, c
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < row and 0 <= nc < col):
                continue
            if (nr, nc) in dist:
                continue
            if board[nr][nc] == 'x':
                continue
            Q.append((nr, nc))
            dist[(nr, nc)] = dist[(r, c)] + 1
    return -1, -1, -1

def dfs(r, c, cnts, dist):
    global board, min_dist, row, col, visited

    if cnts <= 0:
        min_dist = min(min_dist, dist)
        return
    if dist > row*col:
        min_dist = -1
        return
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not (0 <= nr < row and 0 <= nc < col):
            continue
        if board[nr][nc] == 'x':
            continue
        if (nr, nc) in visited:
            continue
        
        temp = [row[:] for row in board]
        visited.append((nr, nc))
        if board[nr][nc] == '*':
            board[nr][nc] = '.'
            cnts -= 1
        dfs(nr, nc, cnts, dist+1)
        visited.pop()
        board = [row[:] for row in temp]


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
prints = []

while True:
    col, row = map(int, input().split())
    if (col, row) == (0, 0):
        break
    board = [list(input()) for _ in range(row)]
    targets = []
    cnt, dist = 0, 0
    min_dist = float('inf')

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'o':
                sr, sc = i, j
            elif board[i][j] == '*':
                targets.append((i, j))
                cnt += 1

    flag = 0
    # for _ in range(cnt):
    #     # sr, sc, min_dist = get_dist(sr, sc, targets)
    #     # min_dist, sr, sc = bfs(sr, sc)
        
    #     board[sr][sc] = '.'
    #     if min_dist == -1:
    #         flag = 1
    #         break
    #     dist += min_dist

    # if flag == 0:
    #     prints.append(dist)
    # else:
    #     prints.append(-1)
    visited = [(sr, sc)]
    dfs(sr, sc, cnt, 0)
    prints.append(min_dist)
    

for each in prints:
    print(each)



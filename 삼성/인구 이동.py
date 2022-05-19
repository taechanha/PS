def dfs(r, c):
    global visited
    S = [(r, c)]
    visited[r][c] = True
    union = [(r, c)]
    while S:
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc]:
                continue
            if not (L <= abs(board[r][c]-board[nr][nc]) <= R):
                continue
            S.append((nr, nc))
            visited[nr][nc] = True
            union.append((nr, nc))
    return union


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
days = 0

while True:
    visited = [[False] * 50 for _ in range(50)]
    unions = []

    # 연합국 계산
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            union = dfs(i, j)
            if len(union) == 1:
                continue
            unions.append(union)  # 연합국들 반환

    # 인구 이동 불가
    # print(unions)
    if unions == []:
        break
    days += 1

    # 인구 이동
    for union in unions:
        sum_union = sum(map(lambda x: board[x[0]][x[1]], union))
        len_union = len(union)
        for i in range(len_union):
            r, c = union[i][0], union[i][1]
            board[r][c] = sum_union // len_union

# 출력: 인구 이동이 몇 일동안 발생하는지
print(days)

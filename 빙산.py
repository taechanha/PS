# 4:11 pm ~ 5:19

# 빙산_org는 처음에 짰던, 불필요한 for문 개선하지 않은 코드 - 더 깔끔

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
T = 0


def dfs(r, c):
    global visited
    stack = [(r, c)]
    visited[r][c] = True
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == 0:
                continue
            stack.append((nr, nc))
            visited[nr][nc] = True


while True:
    T += 1
    temp = [[0] * m for _ in range(n)]

    # 1. 빙산이 녹는다; temp board에 녹은 결과 적용
    if T == 1:
        coord_list = []
        for r in range(n):
            for c in range(m):
                if board[r][c] == 0:
                    continue
                cnt = 0
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if board[nr][nc] == 0:
                        cnt += 1
                temp[r][c] = max(0, board[r][c]-cnt)
                # Refine
                if temp[r][c] > 0:
                    coord_list.append((r, c))
    else:
        new_coord_list = []
        for coord in coord_list:
            r, c = coord  # remember
            if board[r][c] == 0:
                continue
            cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                if board[nr][nc] == 0:
                    cnt += 1
            temp[r][c] = max(0, board[r][c]-cnt)
            # Refine
            if temp[r][c] > 0:
                new_coord_list.append((r, c))
        # remember
        coord_list = new_coord_list[:]
        if coord_list == []:
            print(0)
            exit()

    board = [row[:] for row in temp]
    # 2. 두 덩어리 이상으로 갈라졌는지 체크
    visited = [[False] * m for _ in range(n)]
    chunk = 0
    for coord in coord_list:
        r, c = coord
        if visited[r][c]:
            continue
        if board[r][c] == 0:
            continue
        chunk += 1
        if chunk >= 2:
            print(T)
            exit()
        dfs(r, c)

# 3. 빙산이.. 아예.. 없다..? => 0 출력 == while 벗어날 때까지 출력 못했으면 그게 이거
print(0)

# 10 * (90,000 * 4 + 90,000) = 4,500,000   =>  그냥 나이브하게 구현해도 해결 가능

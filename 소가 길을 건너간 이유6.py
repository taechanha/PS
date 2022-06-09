# 6:27 ~ 7:15

# 0  0   0
# 0  1 - 1
#        |
# 0  0 - 1

from collections import deque
import sys


def dfs(r, c):
    S = [(r, c)]
    visited = [[False] * n for _ in range(n)]
    reached = set()
    reached.add((r, c))
    while S:
        
        r, c = S.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if visited[nr][nc]:
                continue
            if (min(r, nr), min(c, nc), max(r, nr), max(c, nc)) in walls:
                continue
            if board[nr][nc] == 1:
                reached.add((nr, nc))
            S.append((nr, nc))
            visited[nr][nc] = True
    return reached

# 그 길은 못 지나가게
# 지나간 애들만 반환
# 총 리스트에서, 지나가지 못했던 애들 set에 추가


dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
n, k, r = map(int, input().split())
walls = set()
for _ in range(r):
    r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())
    walls.add((min(r1, r2), min(c1, c2), max(r1, r2), max(c1, c2)))
board = [[0] * n for _ in range(n)]
cows = set()
for _ in range(k):
    r, c = map(lambda x: int(x)-1, input().split())
    board[r][c] = 1
    cows.add((r, c))

ans = set()
for r in range(n):
    for c in range(n):
        if board[r][c] != 1:
            continue
        reached: set = dfs(r, c)
        for xr, xc in cows.difference(reached):
            ans.add((min(r, xr), min(c, xc), max(r, xr), max(c, xc)))

print(len(ans))


###


"""
  정해진 길을 이용해야하는 소들 쌍
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(r1, c1):
    dq = deque()
    dq.append((r1, c1))
    cow_visit[r1][c1] = True
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y
            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if cow_visit[nx][ny]:  # 방문 체크
                continue
            if (nx, ny) in road[x][y]:  # 다리인 경우 pass
                continue
            dq.append((nx, ny))
            cow_visit[nx][ny] = True


n, k, r = map(int, sys.stdin.readline().split())  # n*n, k: 마리, r: 정해진 길

road = [[[] for _ in range(n)] for _ in range(n)]
cow_visit = [[False] * n for _ in range(n)]
count = 0
# 길 위치 담기
for _ in range(r):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    road[r1 - 1][c1 - 1].append((r2 - 1, c2 - 1))
    road[r2 - 1][c2 - 1].append((r1 - 1, c1 - 1))

# 소의 위치 담기
cow_list = list()
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    cow_list.append((a - 1, b - 1))

# 1. 소를 한마리씩 돌려가면서 방문 여부 탐색
for i, cow in enumerate(cow_list):
    cow_visit = [[False] * n for _ in range(n)]
    # 2. 현재 소가 정해진 길 없이 가는 경로를 탐색
    bfs(cow[0], cow[1])
    for r2, c2 in cow_list[i + 1:]:
        # 3. 방문을 완료하지 못한 경우 결과 + 1
        if not cow_visit[r2][c2]:
            count += 1
print(count)

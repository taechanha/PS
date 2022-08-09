# 4:30 ~ 5:00

# dp를 사용하지 않고, 움직인 뒤, 벽이 직사각형 내에 존재하는 지를 체크함으로써
# 시간초과를 없앰

from collections import deque
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[False] * M for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 시간초과를 막기 위해 미리 벽을 저장해둔다.
walls = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            walls.append((i, j))

# 저장해둔 벽이 직사각형 범위 내에 있다면 False를 반환
def check(i, j):
    for w_row, w_col in walls:
        if i <= w_row < i+H and j <= w_col < j+W:
            return False
    return True


def bfs():
    q = deque()
    q.append((Sr - 1, Sc - 1, 0))

    while q:
        y, x, cnt = q.popleft()
        visited[y][x] = True

        if y == Fr-1 and x == Fc-1:
            print(cnt)
            return

        for l in range(4):
            yy = dy[l] + y
            xx = dx[l] + x
            # 직사각형 범위계산
            if not (0 <= yy < N and 0 <= xx < M and 0 <= yy + H - 1 < N and 0 <= xx + W - 1 < M):
                continue
            if visited[yy][xx]:
                continue
            if not check(yy, xx):
                continue
            visited[yy][xx] = True
            q.append((yy, xx, cnt+1))

    print(-1)
    return

bfs()
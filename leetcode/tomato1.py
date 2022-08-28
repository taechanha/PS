from collections import deque


def is_in_boundary(x, y):
    return 0 <= x < n and 0 <= y < m

# CASES
# 1) 저장될 때 부터 모두 익어있는 경우
# 2) 고립되어서 익는게 불가능한 경우
# 3) 시간이 지나면 모두 익는 경우

# bfs
# if nothing changes after a iteration -> return -1: 1,2) 커버함


def bfs(G, coordinate_one):
    q = deque([*coordinate_one])
    for x, y in coordinate_one:
        counter[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_in_boundary(nx, ny):
                continue
            # if cnt == some number -> cntnue
            if counter[nx][ny] != 0:
                continue
            if grid[nx][ny] == -1:
                continue

            q.append([nx, ny])
            counter[nx][ny] = counter[x][y] + 1

        print(counter)


def find_zero(grid):
    found = False
    for row in grid:
        found = found or (0 in row)
    return found


def find_max(counter):
    max_list = [max(row) for row in counter]
    return max(max_list) - 1


# 가로, 세로
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# deepcopy of 2D
counter = [row[:] for row in grid]  # [[0] * m for _ in range(n)]

# grid[x][y]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

coordinate_one = []
# get all 1's coord
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            coordinate_one.append([i, j])

# case 1) if 0 not in grid -> print 0
if not find_zero(grid):
    print(0)
    exit()

# do bfs: update counter
bfs(grid, coordinate_one)

# case 2) bfs를 돌았음에도 counter에 0이 있다면, 도달 불가능한 곳이 있다는 말 == 토마토가 익지 않음.
if find_zero(counter):
    print(-1)
    exit()

# case 3) counter에 토마토가 익은 날짜들이 박혀있음. counter 돌면서 max 값 뽑아내고 print.
print(find_max(counter))

# print(counter)

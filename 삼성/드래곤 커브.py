
n = int(input())
size = 101
board = [[0] * size for _ in range(size)]
# 우 상 좌 하
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
maps = {0: 2, 2: 0,
        1: 3, 3: 1}

# 좌표 리스트 계산
def get_coords(x, y, d, g):
    coords = [(x, y)]
    dirs = []
    # 현재 위치에서, 방향 따라 1번 이동: 0세대
    nx = x + dx[d]
    ny = y + dy[d]
    coords.append((nx, ny))
    dirs.append(d)
    if g == 0:
        return coords
    # 2번 이동: 1세대
    nx = nx + dx[(d+1) % 4]
    ny = ny + dy[(d+1) % 4]
    coords.append((nx, ny))
    dirs.append((d+1) % 4)
    if g == 1:
        return coords

    # 그 다음부터는 방향 상관없이 자동
    ret = pattern(nx, ny, g-1, dirs)
    return coords + ret


def pattern(x, y, g, dirs):
    global maps
    coords = []
    for _ in range(g):
        temp_dirs = []
        half = len(dirs)//2
        for i in dirs[:half]:
            x = x + dx[maps[i]]
            y = y + dy[maps[i]]
            coords.append((x, y))
            temp_dirs.append(maps[i])
        for i in dirs[half:]:
            x = x + dx[i]
            y = y + dy[i]
            coords.append((x, y))
            temp_dirs.append(i)
        dirs += temp_dirs
    return coords


# 좌표 리스트를 통해 격자 위에 표시
def draw(coords):
    global board
    for x, y in coords:
        board[y][x] = 1

# 정답 계산
def answer():
    global board, size
    cnt = 0
    for y in range(size-1):
        for x in range(size-1):
            for i, j in ((0, 0), (0, 1), (1, 0), (1, 1)):
                if not board[y+i][x+j] == 1:
                    break
            else:
                cnt += 1
    return cnt

for _ in range(n):
    x, y, d, g = map(int, input().split())

    coords = get_coords(x, y, d, g)
    draw(coords)

print(answer())
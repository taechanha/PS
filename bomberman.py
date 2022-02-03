def is_in_boundary(x, y):
    return 0 <= x < r and 0 <= y < c


def init_time_grid():
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                time_grid[i][j] = 3


def set_bomb(current_time):
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                continue
            grid[i][j] = 'O'
            time_grid[i][j] = current_time + 3


def boom_bomb(current_time):
    for i in range(r):
        for j in range(c):
            if time_grid[i][j] == current_time:
                grid[i][j] = '.'
                time_grid[i][j] = 0
                for k in range(4):
                    current_x = i + dx[k]
                    current_y = j + dy[k]

                    if not is_in_boundary(current_x, current_y):
                        continue

                    grid[current_x][current_y] = '.'


# row, column, time
r, c, n = map(int, input().split())
# right, left, down, up
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# init grid, time_grid
grid = [list(input()) for _ in range(r)]
time_grid = [[0 for _ in range(c)] for _ in range(r)]
init_time_grid()

# do the simulation
time = 2
while True:

    if time == n + 1:
        break

    if time % 2 == 0:
        set_bomb(time)
    else:
        boom_bomb(time)

    time += 1

# print as the mentioned format
for i in range(r):
    for j in range(c):
        print(grid[i][j], end='')
    print()

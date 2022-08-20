a, b = map(int, input().split())
maps = [[0 for _ in range(a)] for _ in range(b)]
n, m = map(int, input().split())
robot = [0]
direct = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n+1):
    x, y, d = input().split()
    x, y = int(x)-1, int(y)
    maps[b-y][x] = i
    robot.append((b-y, x, direct[d]))
orders = []
for _ in range(m):
    rb, o, repeat = input().split()
    orders.append((int(rb), o, int(repeat)))
for order in orders:
    rb, o, repeat = order
    if o == 'F':
        for _ in range(repeat):
            x, y, d = robot[rb]
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= b or ny < 0 or ny >= a:
                print('Robot '+str(rb)+' crashes into the wall')
                exit()
            if maps[nx][ny] != 0:
                print('Robot '+str(rb)+' crashes into robot '+str(maps[nx][ny]))
                exit()
            maps[x][y], maps[nx][ny] = 0, rb
            robot[rb] = (nx, ny, d)
    elif o == 'L':
        x, y, d = robot[rb]
        for _ in range(repeat):
            d = (d+3)%4
        robot[rb] = (x, y, d)
    elif o == 'R':
        x, y, d = robot[rb]
        for _ in range(repeat):
            d = (d+1)%4
        robot[rb] = (x, y, d)
print('OK')
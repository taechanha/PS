class Robot:
    def __init__(self, y1, x1, y2, x2) -> None:
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2

    def move(self, i):
        return Robot(self.y1 + dy[i], self.x1 + dx[i], self.y2 + dy[i], self.x2 + dx[i])

    def rotate(self, i):
        return (Robot(self.y1, self.x1, self.y1+dy[i], self.x1+dx[i]),
                Robot(self.y2, self.x2, self.y2+dy[i], self.x2+dx[i]))

    def position(self):
        return self.y1, self.x1, self.y2, self.x2


def moved(robot):
    ret = []
    for i in range(4):
        ret.append(robot.move(i))
    return ret


def rotated(robot):
    ret = []
    for i in range(4):
        # 방향 D에 대하여 평행이동이 가능하면
        # 방향 D에 대한 회전 2가지 모두 가능
        if is_validated(*robot.move(i).position()):
            first, second = robot.rotate(i)
            ret.append(first)
            ret.append(second)
    return ret


def is_validated(y1, x1, y2, x2):
    def is_wall(y, x):
        return board[y][x] == 1

    def out_of_boundary(y, x):
        return not(0 <= x < n and 0 <= y < n)

    if out_of_boundary(y1, x1):
        return False
    if out_of_boundary(y2, x2):
        return False
    if is_wall(y1, x1):
        return False
    if is_wall(y2, x2):
        return False
    return True


def bfs(robot: Robot):
    q = [robot]
    dist = dict()
    dist[robot.position()] = 0
    end = (n-1, n-1)
    while q:
        curr_robot: Robot = q.pop(0)
        curr_dist = dist[curr_robot.position()]
        y1, x1, y2, x2 = curr_robot.position()
        if (y1, x1) == end or (y2, x2) == end:
            return curr_dist

        explores: list[Robot] = rotated(curr_robot) + moved(curr_robot)
        for explore in explores:
            if not is_validated(*explore.position()):
                continue
            if explore.position() in dist:
                continue
            # print(explore.position())
            q.append(explore)
            dist[explore.position()] = curr_dist + 1


def solution(board):
    global n, m
    n, m = len(board), len(board[0])
    robot = Robot(0, 0, 0, 1)
    cnt = bfs(robot)
    return cnt
    # 격자
    # 최소 시간: bfs
    # 회전, 이동에 각각 1초
    # 회전 시 회전하는 경로에 벽 없어야.
    # 로봇은 상태에 따라 (1, 2) or (2, 1) 차지
    # 첫 위치: (1, 1) (1, 2)


# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
res = solution(board)
print(res)

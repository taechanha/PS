class Robot:
    def __init__(self, r, c, dir) -> None:
        self.r = r
        self.c = c
        self.dir = dir
        self.rotate_cnt = 0
        self.back = {
            0: 2,
            2: 0,
            1: 3,
            3: 1
        }

    def move(self):
        global board
        left = (self.dir - 1) % 4
        nr = self.r + dr[left]
        nc = self.c + dc[left]
        if board[nr][nc] != 2 and board[nr][nc] != 1:
            self.dir = left
            self.r, self.c = nr, nc
            self.rotate_cnt = 0
            return True
        else:
            self.dir = left
            self.rotate_cnt += 1
            if self.rotate_cnt == 4:
                back = self.back[self.dir]
                nr = self.r + dr[back]
                nc = self.c + dc[back]
                if board[nr][nc] == 1:
                    return False
                else:
                    self.r, self.c = nr, nc
                    self.rotate_cnt = 0
        return True


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
robot = Robot(r, c, d)
cnt = 0
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

should_continue = True
while should_continue:
    # 현재 위치 청소
    if board[robot.r][robot.c] != 2:
        board[robot.r][robot.c] = 2
        cnt += 1
    # 로봇 이동
    should_continue = robot.move()

print(cnt)
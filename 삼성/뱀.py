from collections import deque


class Snake:
    def __init__(self, r, c, dir, tail=deque()) -> None:
        # head
        self.r = r
        self.c = c
        self.dir = dir
        # tail
        self.tail = tail

    def move(self, dir):
        global board, should_continue
        # 방향 결정
        dir = self.dir + rotate[dir]
        if dir == -1:
            dir = 3
        if dir == 4:
            dir = 0
        # 이동
        self.dir = dir
        nr = self.r + dr[dir]
        nc = self.c + dc[dir]
        # 벽?
        if not (0 <= nr < n and 0 <= nc < n):
            should_continue = False
            return
        # 자기 몸?
        if (nr, nc) in self.path:
            should_continue = False
            return

        # 사과?
        if board[nr][nc] == 1:
            self.tail.append((self.r, self.c))
            board[nr][nc] = 0  # 실수 1
        else:
            if self.tail:
                self.tail.popleft()
                self.tail.append((self.r, self.c))  # 실수 2

        # 이동 완료
        self.r = nr
        self.c = nc


n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    r, c = map(lambda x: int(x) - 1, input().split())
    board[r][c] = 1
l = int(input())
moves = deque()
for _ in range(l):
    move, dir = input().split()
    moves.append([int(move), dir])

rotate = {
    'INIT': 0,
    'L': -1,
    'D': 1,
}
should_continue = True
secs = 0
# 우하좌상
dir = 'INIT'
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
snake = Snake(0, 0, 0)

while should_continue:

    if moves and secs == moves[0][0]:
        _, dir = moves.popleft()

    snake.move(dir)
    dir = 'INIT'

    secs += 1

print(secs)

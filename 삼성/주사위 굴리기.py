n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(lambda x: int(x) - 1, input().split()))

# 이동 - 칸: 0 -> 바닥면이 칸으로 복사, 칸: O이 아니면 -> 칸 숫자가 바닥면으로 복사되고, 칸 숫자는 0으로
# 칸 밖 이동 불가 -> 출력도 x
# 이동 시 마다 상단의 숫자 출력

# 동 서 북 남
# 1  2 3 4
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

#   2
# 4 1 3
#   5
#   6


class Dice:
    def __init__(self, r, c) -> None:
        self.r, self.c = r, c
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0
        self.up = 0
        self.down = 0

    def move(self, dir):
        global board
        nr = self.r + dr[dir]
        nc = self.c + dc[dir]
        if not (0 <= nr < n and 0 <= nc < m):
            return
        # 주사위 상태 & 위치 변화
        self.change_state(dir)
        self.r, self.c = nr, nc
        # 문제 조건
        if board[nr][nc] == 0:
            board[nr][nc] = self.down
        else:
            self.down = board[nr][nc]
            board[nr][nc] = 0
        print(self.up)

    def change_state(self, dir):
        # 동 서 북 남
        if dir == 0:
            self.east, self.down, self.west, self.up = self.up, self.east, self.down, self.west
        elif dir == 1:
            self.west, self.down, self.east, self.up = self.up, self.west, self.down, self.east
        elif dir == 2:
            self.north, self.down, self.south, self.up = self.up, self.north, self.down, self.south
        else:
            self.south, self.down, self.north, self.up = self.up, self.south, self.down, self.north


dice = Dice(x, y)
for dir in moves:
    dice.move(dir)

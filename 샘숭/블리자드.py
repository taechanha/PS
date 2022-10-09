# 초기 상태: 위가 1, 3이 동쪽, (0, 0)에 위치, 첫 이동방향: 동쪽
# 1. 이동 방향으로 한 칸 이동, 없으면 반대 방향으로 방향을 바꾼 다음 한 칸 이동
# 2. 도착한 칸에 대한 점수 획득
#  (r, c)의 정수 B, (r, c)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 개수 C
#  이동할 수 있는 칸: 그 칸이 B
#  최종 점수: B*C
# 3. 다음 이동 방향: 주사위 아랫면 A, 주사위가 있는 칸 (r, c)의 정수 B
#  A > B: 이동 방향 90도 시계방향 회전
#  A < B: 이동 방향 90도 반시계방향 회전
#  A = B: 이동 방향 변화 없음
# 출력: 모든 이동에서 획득하는 점수의 합

#   2
# 4 1 3
#   5
#   6

def pnt(dice):
    asd = {0: '상', 1: "우", 2: "하", 3: "좌"}
    print("pos:", dice.pos)
    print("dir:", asd[dice.dir])
    print("score:", dice.totalScore)
    print(f"   {dice.north}   ")
    print(f" {dice.west} {dice.up} {dice.east}")
    print(f"   {dice.south}   ")
    print(f"   {dice.down}   ")
    print("--------------------")


class Dice:
    def __init__(self, r, c, dir):
        self.pos = [r, c]
        self.dir = dir  # 0: 상, 1: 우, 2: 하, 3: 좌
        self.up = 1
        self.north = 2
        self.east = 3
        self.south = 5
        self.west = 4
        self.down = 6
        self.reverseDir = {0: 2, 2: 0, 1: 3, 3: 1}
        self.rotate90 = {0: 1, 1: 2, 2: 3, 3: 0}
        self.rotateM90 = {nxt: cur for cur, nxt in self.rotate90.items()}
        self.totalScore = 0

    def move(self):
        global R, C
        """
        chg: pos, dir(possible), up~down
        """
        r, c = self.pos
        if self.dir == 1:  # ->
            if (0 <= r < R and 0 <= c+1 < C):
                self.west, self.up, self.east, self.down = self.down, self.west, self.up, self.east
                self.pos = [r, c+1]
            else:
                # 반대 방향 전환 후 이동
                self.dir = self.reverseDir[self.dir]
                self.west, self.up, self.east, self.down = self.up, self.east, self.down, self.west
                self.pos = [r, c-1]

        elif self.dir == 3:  # <-
            if (0 <= r < R and 0 <= c-1 < C):
                self.west, self.up, self.east, self.down = self.up, self.east, self.down, self.west
                self.pos = [r, c-1]
            else:
                # 반대 방향 전환 후 이동
                self.dir = self.reverseDir[self.dir]
                self.west, self.up, self.east, self.down = self.down, self.west, self.up, self.east
                self.pos = [r, c+1]

        elif self.dir == 0:  # up
            if (0 <= r-1 < R and 0 <= c < C):
                self.north, self.up, self.south, self.down = self.up, self.south, self.down, self.north
                self.pos = [r-1, c]
            else:
                # 반대 방향 전환 후 이동
                self.dir = self.reverseDir[self.dir]
                self.north, self.up, self.south, self.down = self.down, self.north, self.up, self.south
                self.pos = [r+1, c]

        elif self.dir == 2:  # down
            if (0 <= r+1 < R and 0 <= c < C):
                self.north, self.up, self.south, self.down = self.down, self.north, self.up, self.south
                self.pos = [r+1, c]
            else:
                # 반대 방향 전환 후 이동
                self.dir = self.reverseDir[self.dir]
                self.north, self.up, self.south, self.down = self.up, self.south, self.down, self.north
                self.pos = [r-1, c]

    def setScore(self):
        """ chg: totalscore """
        global R, C, board
        r, c = self.pos
        S = [(r, c)]
        visited = [[False for _ in range(C)] for __ in range(R)]
        visited[r][c] = True
        baseScore = board[r][c]
        cnt = 1
        while S:
            r, c = S.pop()
            for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if visited[nr][nc]:
                    continue
                compareScore = board[nr][nc]
                if baseScore != compareScore:
                    continue
                S.append((nr, nc))
                visited[nr][nc] = True
                cnt += 1
        self.totalScore += cnt * baseScore

    def setNextDir(self):
        """ chg: dir, up~down """
        r, c = self.pos
        floorScore = board[r][c]
        diceScore = self.down
        if diceScore > floorScore:
            self.dir = self.rotate90[self.dir]
        elif diceScore < floorScore:
            self.dir = self.rotateM90[self.dir]


R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
ans = 0
r, c, dir = 0, 0, 1
dice = Dice(r, c, dir)
while K:
    K -= 1
    dice.move()
    dice.setScore()
    dice.setNextDir()

print(dice.totalScore)

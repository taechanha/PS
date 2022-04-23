# 윗면: 1, 동쪽을 바라보는 방향: 3
# 좌표: 1, 1
# 첫 이동 방향: 동쪽
# 칸 (x, y)에 대한 점수를 구하는 방법: 현재 위치 (x, y)에 있는 보드 위에 점수가 B, 현재 위치에서 동서남북 방향으로
#   연속해서 이동할 수 있는 칸의 수 C, 이 칸들에는 모두 B가 있어야, C x B가 (x, y)에서 얻을 수 있는 점수
#   -> 동서남북 다 합한 값이겠지?

# 고려해야할 것
# - 연속해서 이동할 수 있는 칸: 그냥 현재 위치에서 bfs 후 거쳐간 칸의 개수
# - 주사위 이동 시 마다 방향 바뀌는 것

# 문제: 각 이동에서 획득하는 점수의 합


class state:
    def __init__(self, east, west, up, down, north, south):
        self.east = east
        self.west = west
        self.up = up
        self.down = down  # 바닥면
        self.north = north
        self.south = south


class dice:
    def __init__(self, r, c, dir, east, west, up, down, north, south):
        self.r = r
        self.c = c
        self.dir = dir
        self.state = state(east, west, up, down, north, south)

    def move(self):
        nr = self.r + dr[self.dir]
        nc = self.c + dc[self.dir]
        if 0 <= nr < N and 0 <= nc < M:
            # 주사위 이동
            self.r = nr
            self.c = nc
            # 주사위 상태 변화
            self.change_state()
            # print(self.r, self.c, nr, nc)
            # 이 함수의 termination point.
        else:
            if self.dir == 0:
                self.dir = 1
            elif self.dir == 1:
                self.dir = 0
            elif self.dir == 2:
                self.dir = 3
            elif self.dir == 3:
                self.dir = 2
            self.move()

    def change_state(self):
        # 위쪽으로 이동한다면,
        if self.dir == 0:
            # 변하는 것: north, up, down, south. 어떻게?
            self.state.north, self.state.down, self.state.south, self.state.up = \
                self.state.up, self.state.north, self.state.down, self.state.south
        # 아래쪽으로 이동한다면,
        elif self.dir == 1:
            # print("BEFORE:")
            # print(" ", DICE.state.north)
            # print(DICE.state.west, DICE.state.up, DICE.state.east)
            # print(" ", DICE.state.south)
            # print(" ", DICE.state.down)

            self.state.north, self.state.down, self.state.south, self.state.up = \
                self.state.down, self.state.south, self.state.up, self.state.north

            # print()
            # print("AFTER:")
            # print(" ", DICE.state.north)
            # print(DICE.state.west, DICE.state.up, DICE.state.east)
            # print(" ", DICE.state.south)
            # print(" ", DICE.state.down)

        # 오른쪽으로 이동한다면,
        elif self.dir == 2:
            self.state.west, self.state.down, self.state.east, self.state.up = \
                self.state.up, self.state.west, self.state.down, self.state.east

        # 왼쪽으로 이동한다면,
        elif self.dir == 3:
            self.state.west, self.state.down, self.state.east, self.state.up = \
                self.state.down, self.state.east, self.state.up, self.state.west

    def change_direction(self, A, B):
        # A > B: 시계 90도
        # 상하좌우
        # 상->우: 0->3
        # 하->좌: 1->2
        # 좌->상: 2->0
        # 우->하: 3->1
        if A > B:
            if self.dir == 0:
                self.dir = 3
            elif self.dir == 1:
                self.dir = 2
            elif self.dir == 2:
                self.dir = 0
            elif self.dir == 3:
                self.dir = 1
        # A < B: 반시계 90도
        # 상->좌: 0->2
        # 하->우: 1->3
        # 좌->하: 2->1
        # 우->상: 3->0
        elif A < B:
            if self.dir == 0:
                self.dir = 2
            elif self.dir == 1:
                self.dir = 3
            elif self.dir == 2:
                self.dir = 1
            elif self.dir == 3:
                self.dir = 0

        # A == B: 변화 없음 -> do nothing


def dfs(r, c, curr_board):
    stack = [(r, c)]  # 시작점
    visited = [(r, c)]
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                # print("not case1: ", nr, nc)
                continue
            if (nr, nc) in visited:
                # print("not case2: ", nr, nc)
                continue
            if not (board[nr][nc] == curr_board):
                # print("not case3: ", nr, nc, board[nr][nc], curr_board)
                continue
            stack.append((nr, nc))
            visited.append((nr, nc))

    # print("visited: ", visited)
    return len(visited)


global N, M, K
N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
score = 0
# init dice
DICE = dice(r=0, c=0, dir=3, east=3, west=4, up=1, down=6, north=2, south=5)

while K:
    K -= 1

    # 1. 주사위 이동(이동하려는 곳에 벽 있으면 반대로 돌려서 한 칸 이동) + 방향 수정
    DICE.move()  # : 이동 -> 현재 방향(dir)에 따라 좌표 변화(r=nr, c=nc) & 숫자 방향 변화

    # 2. 도착한 칸에서 점수 획득 - dfs
    count = dfs(DICE.r, DICE.c, board[DICE.r][DICE.c])
    score += (board[DICE.r][DICE.c] * count)

    # print(" ", DICE.state.north)
    # print(DICE.state.west, DICE.state.up, DICE.state.east)
    # print(" ", DICE.state.south)
    # print(" ", DICE.state.down)
    # print("direction: ", DICE.dir)
    # print("position: ", DICE.r, DICE.c, "\n")

    # 3. 주사위의 이동 방향 결정
    DICE.change_direction(DICE.state.down, board[DICE.r][DICE.c])


print(score)

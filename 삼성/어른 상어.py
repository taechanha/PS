# 매 초마다 상어가 이동
# 이동 후 같은 칸에 복수 개의 상어가 있다면 가장 작은 번호 상어를 제외한 나머지 상어는 삭제
# 초기에 냄새 뿌림, 이후 이동 후 냄새 뿌림, 냄새에는 상어 번호와 k초
# 이동 방향 결정
#     - 인접한 칸 중 냄새 없는 칸
#     - 그런 칸이 없으면 자신의 냄새가 있는 칸
#     - 가능한 칸이 여러 개면 각 상어당 할당된 우선순위 따라 이동
#     - 상어마다 다르고, 각 상어의 현재 방향따라 다름

# 정답: 1번 상어만 격자에 남게 되기까지 걸리는 시간
#       1000초가 넘어도 여러 마리의 상어가 있으면 -1 출력

def should_terminate():
    global shark_list, sec
    if len(shark_list) == 1 and shark_list[0].idx == 0:
        return True
    if sec > 1000:
        return True
    return False


def out_of_bound(r, c):
    return not(0 <= r < N and 0 <= c < N)


def smell_decrease():
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                if smell[i][j].just_moved:
                    smell[i][j].just_moved = False
                    continue
                elif smell[i][j].sec_left >= 1:
                    smell[i][j].sec_left -= 1
                if smell[i][j].sec_left == 0:
                    smell[i][j] = None


class Shark:
    def __init__(self, idx=None, r=None, c=None, dir=None, dir_prty=None) -> None:
        self.idx = idx
        self.r = r
        self.c = c
        self.dir = dir
        self.dir_prty = dict()

    def move(self):
        global K
        # ******************************************************************
        # 앞으로 메소드에서 사용하는 클래스 변수는 대문자로 여기에 미리 정의해놓고 사용.
        # self.dir_ptry[self.dir]로 써야할 것을 [dir]로 써서 전역변수 값을 가져왔음.
        # 이 실수 반복해서 일어나고 있음
        # ******************************************************************
        # 0  1  2  3
        # 위 아래 왼 오
        # 인접한 칸 조사
        new_r, new_c = None, None
        # 여러 개면, 우선순위대로 이동 - 애초부터 우선순위 대로 탐색
        for i in self.dir_prty[self.dir]:
            nr = self.r + dr[i]
            nc = self.c + dc[i]
            if out_of_bound(nr, nc):
                continue
            # 삭제
            # 실수 2: 각 플레이에서, 뒷 번호 상어가 앞 번호 상어를 피해감(냄새있으니까)
            # 그래서 get-around로, left_sec이 4이면, 같은 위치에 놓고 리턴함 -> 삭제 구현에 의존
            if smell[nr][nc]:
                if smell[nr][nc].sec_left == 4:
                    self.r = nr
                    self.c = nc
                    return
            # 냄새있는지
            if not smell[nr][nc]:
                new_r, new_c = nr, nc
                break
            # 모두 다 냄새있으면, 자신의 냄새가 있는 칸으로
            if smell[nr][nc] and smell[nr][nc].shark_idx == self.idx:
                if new_r == None and new_c == None:
                    new_r, new_c = nr, nc
        # 방향 결정
        self.set_dir(new_r, new_c)
        # 이동
        self.r = new_r
        self.c = new_c
        # 기존 냄새 시간 감소
        # X
        # 냄새 생성
        smell[self.r][self.c] = Smell(self.idx, K, True)

    def set_dir(self, new_r, new_c):
        # 0 1 2 3: 위 아래 왼 오른
        try:
            diff_r = new_r - self.r
        except:
            print(new_r, self.r)

        diff_c = new_c - self.c
        if diff_r == -1:
            self.dir = 0
        if diff_r == 1:
            self.dir = 1
        if diff_c == -1:
            self.dir = 2
        if diff_c == 1:
            self.dir = 3

    def __str__(self):
        return str(self.idx) + " " + str(self.r) + " " + str(self.c) + " " + str(self.dir) + " " + str(self.dir_prty)


class Smell:
    def __init__(self, shark_idx, sec_left, just_moved) -> None:
        self.shark_idx = shark_idx
        self.sec_left = sec_left
        self.just_moved = just_moved

    def __str__(self):
        return "(" + str(self.shark_idx) + ", " + str(self.sec_left) + ")"


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
smell = [[None] * N for _ in range(N)]
dirs = list(map(int, input().split()))
# 위 아래 왼 오른
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
sec = 0
shark_list = []
# current dir
for dir in dirs:
    shark_list.append(Shark(dir=dir-1))
idx = -1
# direction priority
for cnt in range(M * 4):
    if cnt % 4 == 0:
        idx += 1
    a, b, c, d = map(int, input().split())
    shark_list[idx].dir_prty[cnt % 4] = [a-1, b-1, c-1, d-1]
# r, c
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != 0:
            idx = board[row][col] - 1
            shark_list[idx].idx = idx
            shark_list[idx].r = row
            shark_list[idx].c = col

# debug
for shark in shark_list:
    print(shark)
print()
#

for shark in shark_list:
    smell[shark.r][shark.c] = Smell(shark.idx, K, False)

while not should_terminate():
    """
    smell: list[list[Smell]]
    shark_list: list[Shark]
    board: list[list[ -1 or Shark ]]
    """
    temp_smell = [[None] * N for _ in range(N)]
    # 상어 이동
    # 실수 1: 각 shark가 이동할 때마다 냄새 시간 감소시켰음
    for shark in shark_list:
        shark.move()

    # 기존 냄새 시간 감소, 새로운 냄새 생성
    smell_decrease()
    # for i in range(N):
    #     for j in range(N):
    #         if temp_smell[i][j]:
    #             smell[i][j] = temp_smell[i][j]

    # 상어 삭제
    board = [[-1] * N for _ in range(N)]
    shark_list.sort(key=lambda shark: shark.idx)
    for shark in shark_list:
        if board[shark.r][shark.c] == -1:
            board[shark.r][shark.c] = shark
    new_shark_list = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != -1:
                new_shark_list.append(board[i][j])
    shark_list = new_shark_list[:]

    # debug
    print("SHARK")
    for shark in shark_list:
        print(shark)
    print("SMELL")
    for row in smell:
        for col in row:
            print(col, end=" ")
        print()
    print()

    # if sec == 3:
    #     for row in board:
    #         print(row)
    #     exit()
    #
    sec += 1

if sec > 1000:
    print(-1)
else:
    print(sec)

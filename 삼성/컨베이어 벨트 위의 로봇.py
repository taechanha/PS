# 1. 한 칸 회전
# 2. 가장 먼저 올라간 로봇부터 이동 가능
#    - 이동하기 위해서 이동하려는 칸에 로봇이 없고, 내구도가 1 이상이어야
# 3. 올리는 위치 내구도가 1 이상이면 그 위치에 로봇 올리기
# 4. 내구도가 0인 칸이 K개 이상이면 종료

# 회전하면 로봇 같이 움직임
# 로봇이 올리는 위치에 올라가거나, 이동하면 그 칸의 내구도 1 감소
# 올리는 위치에서 올리고 내리는 위치에서 내림

class Robot:
    def __init__(self, c) -> None:
        self.c = c
    
    def move(self):
        global robot_list, conveyer
        for robot in robot_list:
            # 이동하려는 칸에 로봇이 이미 있다면 이동 불가
            if self.c+1 == robot.c:
                return

        # 현재 self.c는 절대 내리는 위치일 수 없음 -> self.c+1는 valid한 연산
        if conveyer[0][self.c+1] > 0:
            conveyer[0][self.c+1] -= 1
            self.c += 1
        

def conveyer_move():
    global row, col, conveyer

    # 윗칸 움직임
    temp = [[0] * col for _ in range(row)]
    for c in range(col):
        if c == col - 1:
            break
        temp[0][c+1] = conveyer[0][c]
    temp[1][col-1] = conveyer[0][c]

    # 아래칸 움직임
    for c in range(col-1, -1, -1):
        if c == 0:
            break
        temp[1][c-1] = conveyer[1][c]
    temp[0][0] = conveyer[1][c]

    conveyer = [row[:] for row in temp]
    return conveyer

def robot_drop():
    global col, robot_list
    remove_robot_idx = None
    for idx, robot in enumerate(robot_list):
        if robot.c == col-1:
            remove_robot_idx = idx
    if remove_robot_idx != None:
        robot_list.pop(remove_robot_idx)


def termination_cond():
    global K, row, col, conveyer
    cnt = 0
    for r in range(row):
        for c in range(col):
            if conveyer[r][c] == 0:
                cnt += 1
    return cnt

# TODO:
# 1. 컨베이어 벨트 움직임 구현 [v]
# 2. 로봇 이동 구현 [v]
# 3. 로봇 올리기/내리기 구현 [v]
# 4. 정답 계산 [v]

N, K = map(int, input().split())
A = list(map(int, input().split()))
conveyer = []
conveyer.append(A[:N])
conveyer.append(A[N:][::-1])
col = len(conveyer[0])
row = len(conveyer)
phase = 0
robot_list = []

while termination_cond() < K:
    phase += 1

    # 컨베이어 움직임
    conveyer = conveyer_move()
    for robot in robot_list:
        robot.c += 1

    # 로봇 내리기
    robot_drop()

    # 로봇 이동
    for robot in robot_list:
        robot.move() # 내구도 반영 동시에

    # 로봇 내리기
    robot_drop()

    # 로봇 올리기
    if conveyer[0][0] > 0:
        conveyer[0][0] -= 1
        robot_list.append(Robot(0))
    
print(phase)



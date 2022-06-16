
# 톱니바퀴 표현
# - 8 방향

# 톱니바퀴 회전
# - 시계: 1
# - 반시계: -1

# 회전 여부
# 회전했으면 인접한 톱니의 맞닿은 극 조사
# -> 인접 톱니 회전 여부

# 출력
# - 1번 톱니바퀴: 12시 방향이 N극이면 0점, S극이면 1점
# - 2: 0, 2
# - 3: 0, 4
# - 4: 0, 8
class Wheel:
    def __init__(self, tooths) -> None:
        # 0  1   2  3  4  5  6  7
        # 북 북동 동 동남 남 서남 서 북서
        self.tooths = tooths[:]

    def rotate(self, dir):
        copy = [0] * 8
        for i in range(8):
            copy[(i+dir) % 8] = self.tooths[i]
        self.tooths = copy[:]


N, S = 0, 1
wheels, ops = [], []
for _ in range(4):
    tooths = list(map(int, input()))
    wheels.append(Wheel(tooths))
k = int(input())
for _ in range(k):
    idx, dir = map(int, input().split())
    ops.append((idx-1, dir))

for op in ops:
    cur, dir = op[0], op[1]
    starting_tooths = [wheel.tooths[:] for wheel in wheels]

    # 왼쪽
    prev_dir = dir
    for i in range(cur, -1, -1):
        # 인접 바퀴 극 같은지, 같지 않으면 그 바퀴도 회전
        if i == 0:
            break
        if starting_tooths[i-1][2] == starting_tooths[i][6]:
            break
        prev_dir = -prev_dir
        wheels[i-1].rotate(prev_dir)

    # 오른쪽
    prev_dir = dir
    for i in range(cur, 4):
        # 인접 바퀴 극 같은지, 같지 않으면 그 바퀴도 회전
        if i == 3:
            break
        if starting_tooths[i][2] == starting_tooths[i+1][6]:
            break
        prev_dir = -prev_dir
        wheels[i+1].rotate(prev_dir)

    # 기준 바퀴
    wheels[cur].rotate(dir)

cnt = 0
for i, wheel in enumerate(wheels):
    if wheel.tooths[0] == S:
        cnt += pow(2, i)

print(cnt)
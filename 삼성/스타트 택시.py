
# 승객 위치, 각 승객의 목적지, 택시 위치

# 택시가 첫 위치에서 승객을 고를 때는 가장 가까운 위치에 있는 승객(BFS)
#   - 여러 명이라면, 그 중 행과 열이 가장 작은 숫자를 가진 승객
#   - 이동 시 칸마다 연료 - 1, 연료가 0이라면 거기서 종료
#   - 도착지에서 연료가 0 이라면 종료 X

# 승객을 태운 후, 거기서부터 목적지까지 BFS
#   - 이동 할 때 마다 연료 - 1
#   - 마찬가지로, 연료 0 이라면 종료, 도착지에서 연료 0인 경우는 종료 X
#   - 목적지에 도착하면, 여기서 소모된 연료의 2배를 충전(더하는 것, 대체가 아님)

# 행과 열 1 ~ N, 따라서 초기 위치 지정 시 -1, -1 해줘야 함

def terminate():
    print(-1)
    exit()


def out_of_bound(r, c):
    return not (0 <= r < N and 0 <= c < N)

# BFS


def to_passenger(r, c):
    INF = float('inf')
    q = [(r, c)]
    dist = dict()
    dist[(r, c)] = 0
    ret = []
    min_dist = INF
    while q:
        r, c = q.pop(0)
        if dist[(r, c)] > min_dist:
            continue
        if (r, c) in passenger_starts:
            ret.append((r, c))
            min_dist = min(min_dist, dist[(r, c)])
        if min_dist != INF and min_dist >= G:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if out_of_bound(nr, nc):
                continue
            if (nr, nc) in dist:
                continue
            if board[nr][nc] == 1:
                continue
            q.append((nr, nc))
            dist[(nr, nc)] = dist[(r, c)] + 1
    return ret, min_dist

# BFS


def to_target(r, c, tr, tc):
    q = [(r, c)]
    dist = dict()
    dist[(r, c)] = 0
    while q:
        r, c = q.pop(0)
        if (r, c) == (tr, tc):
            return tr, tc, dist[(r, c)]
        if dist[(r, c)] >= G:
            continue  # 실수 포인트 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if out_of_bound(nr, nc):
                continue
            if (nr, nc) in dist:
                continue
            if board[nr][nc] == 1:
                continue
            q.append((nr, nc))
            dist[(nr, nc)] = dist[(r, c)] + 1
    return -1, -1, 0


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M, G = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(int, input().split()))
taxi[0], taxi[1] = taxi[0]-1, taxi[1]-1
passenger_starts = []
passenger_targets = []
for _ in range(M):
    sr, sc, tr, tc = map(int, input().split())
    passenger_starts.append((sr-1, sc-1))
    passenger_targets.append((tr-1, tc-1))

PLAYS = len(passenger_starts)
for _ in range(PLAYS):
    # 현재 택시 위치에서 가장 빠른 승객 위치까지 이동
    passenger_candidates, consumed_gas = to_passenger(taxi[0], taxi[1])
    # 가장 빠른 승객 위치 선택
    # 승객 후보가 없는 경우: 도달할 수 없는 경우: 벽에 막힘 / 연료가 없음
    if not passenger_candidates:
        # print("1")
        terminate()
    passenger = sorted(passenger_candidates, key=lambda x: (x[0], x[1]))[0]
    # 연료 소비 적용
    G -= consumed_gas

    # print(passenger, G, consumed_gas)
    # exit()

    # 승객 삭제 처리
    # print(passenger_starts, passenger_targets, passenger)
    delete_idx = 0
    for i in range(len(passenger_starts)):
        if passenger_starts[i] == passenger:
            delete_idx = i
            # 아.........................................................................
            break
    r, c = passenger_starts.pop(delete_idx)
    tr, tc = passenger_targets.pop(delete_idx)
    # print(r, c, tr, tc, i, delete_idx)
    # exit()
    # print("asdasads: ", (r, c), (tr, tc))

    # 현재 태운 승객 위치에서 목적지까지 이동
    # print("to target: ", r, c, (tr, tc))
    r, c, consumed_gas = to_target(r, c, tr, tc)  # 연료 소비 적용

    # print("zxc: ", (r, c), consumed_gas)

    # 만약 목적지까지 이동 불가한 경우
    if (r, c) == (-1, -1):
        # print("target check")
        terminate()

    # 연료 소비 적용
    G -= consumed_gas

    # 소비 연료 2배 충전
    G += consumed_gas * 2

    # 택시 위치 갱신
    taxi[0], taxi[1] = r, c

    # print("r, c, G: ", r, c, G)
# 남아있는 연료
print(G)


# self made TC
# 3 2 7
# 0 0 0
# 0 0 0
# 0 0 0
# 3 1
# 1 1 2 2
# 1 1 3 3

# 3 3 4
# 0 0 0
# 0 0 0
# 0 0 0
# 1 1
# 1 1 3 3
# 1 2 3 3
# 2 2 3 3

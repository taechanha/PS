R, C, M = map(int, input().split())
hooked_sharks = 0
# 위: 0 아래: 1 오른쪽: 2 왼쪽 3
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
maps = {
    0: 1, 1: 0,
    2: 3, 3: 2
}
sharks = []
temp = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append((r-1, c-1, s, d-1, z))
    temp[r-1][c-1] = [s, d-1, z]


def move_shark(shark):
    r, c, s, d, z = shark
    for i in range(s):
        nr = r + dr[d]
        nc = c + dc[d]
        dir = d
        if not (0 <= nr < R and 0 <= nc < C):
            nr = r + dr[maps[d]]
            nc = c + dc[maps[d]]
            dir = maps[d]
        r, c, d = nr, nc, dir
    return (r, c, s, d, z)


# 1. 낚시왕 이동
for fisherman in range(C):
    closest_row = float('inf')
    # 2. 상어 잡기
    to_hook = None
    for i, shark in enumerate(sharks):
        r, c, _, _, _ = shark
        if fisherman != c:
            continue
        if closest_row > r:
            closest_row = r
            to_hook = i
    # 상어 크기 합산
    if to_hook != None:
        hooked_sharks += sharks.pop(to_hook)[-1]

    # 3. 상어 이동
    new_sharks = []
    for shark in sharks:
        new_sharks.append(move_shark(shark))
    # 4. 같은 칸에 상어 있으면 가장 큰 상어 빼고 제거
    temp = [[0] * C for _ in range(R)]
    for r, c, s, d, z in new_sharks:
        if temp[r][c] == 0:
            temp[r][c] = [s, d, z]
            continue
        if temp[r][c][-1] < z:
            temp[r][c] = [s, d, z]

    sharks = []
    for i in range(R):
        for j in range(C):
            if temp[i][j] == 0:
                continue
            s, d, z = temp[i][j]
            sharks.append((i, j, s, d, z))

# 5. 출력: 잡은 상어 크기의 합
print(hooked_sharks)

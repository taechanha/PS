from collections import deque

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rotates = []
for _ in range(t):
    x, d, k = map(int, input().split())
    rotates.append((x-1, d, k))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def rotate_cw(row):
    n = len(row)
    temp = [0] * n
    temp[0] = row[n-1]
    for i in range(0, n-1):
        temp[i+1] = row[i]
    return temp


def rotate_ccw(row):
    n = len(row)
    temp = [0] * n
    temp[n-1] = row[0]
    for i in range(1, n):
        temp[i-1] = row[i]
    return temp


for x, d, k in rotates:
    # board의 각 row에 대해
    for row in range(x, n, x+1):
        if d == 0:
            td = deque(board[row])
            for _ in range(k):
                td.rotate()    # 이렇게 한다고 속도 개선 읎다..
                # board[row] = rotate_cw(board[row])
            board[row] = list(td)
        else:
            for _ in range(k):
                board[row] = rotate_ccw(board[row])

    # DEBUG
    # if (x, d, k) == (1, 0, 2):
    #     print(board)

    temp = [row[:] for row in board]
    flag = 0
    # 인접한 수 모두 지우기
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'x':  # 실수 1
                continue
            # 예외 케이스: r == 0, r == n-1, c == 0, c == m-1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < n):
                    continue
                if not (0 <= nc < m):
                    if nc == -1:
                        nc = m-1
                    elif nc == m:
                        nc = 0
                if board[nr][nc] == 'x':
                    continue

                # 인접하고, 같다면 지우기
                if board[r][c] == temp[nr][nc]:
                    # 인접한 경우 존재 여부
                    flag = 1
                    temp[r][c] = 'x'
                    temp[nr][nc] = 'x'

    board = [row[:] for row in temp]
    # 인접한 수가 없으면 적힌 수의 평균을 구하고, 평균보다 작은 수는 +1, 큰 수는 -1
    if flag == 0:
        summation, cnt = 0, 0
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'x':
                    summation += board[i][j]
                    cnt += 1
        # 평균
        if cnt == 0:
            continue
        mean = summation / cnt  # 실수 2: zero division
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'x':
                    continue
                if board[i][j] > mean:
                    board[i][j] -= 1
                elif board[i][j] < mean:
                    board[i][j] += 1


# 출력: 원판에 적힌 수의 합
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] != 'x':
            cnt += board[i][j]
print(cnt)

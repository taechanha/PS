from typing import List

class data:
    def __init__(self, fires=0, ices=0, temp=0, turn=0):
        self.fires = fires
        self.ices = ices
        self.temp = temp
        self.turn = turn

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    global N
    N = n
    answer = [[]]
    # init
    board = [[0 for _ in range(n)] for __ in range(n)]
    for x, y in fires:
        board[x-1][y-1] = data(fires=1) # f/i, cnt, temperature, 
    for x, y in ices:
        board[x-1][y-1] = data(ices=1)
    
    # calculate
    for turn in range(m):
        # spread
        for x, y in fires:
            fire_visits = go_fire(board, x-1, y-1, turn)
        for x, y in ices:
            ice_visits = go_ice(board, x-1, y-1, turn)
        # count temperature

        cal_temp(board, turn)

        for row in board:
            for r in row:
                if r == 0:
                    print((0, 0, 0), end=' ')
                else:
                    print((r.fires, r.ices, r.temp), end=' ')
            print()
        print()

        fires = fire_visits
        ices = ice_visits
    return answer

def cal_temp(board, turn):
    for r in range(N):
        for c in range(N):
            data = board[r][c]
            if data == 0:
                continue
            if data.fires:
                data.temp += 1
            if data.ices:
                data.temp -= 1
            if data.fires == 3 and data.ices == 1:
                data.temp += 2
                

def go_fire(board, x, y, turn):
    q = [(x, y, 0)]
    visited = [[False for _ in range(N)] for __ in range(N)]
    visited[x][y] = True
    dr, dc = [0, 0, -1, 1, -1, -1, 1, 1], [-1, 1, 0, 0, -1, 1, -1, 1]
    visits = []
    while q:
        r, c, cnt = q.pop()
        if cnt == 1:
            continue
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if oob(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            q.append((nr, nc, cnt+1))
            visited[nr][nc] = True
            visits.append((nr, nc))
            if board[nr][nc] == 0:
                board[nr][nc] = data(fires=1, turn=turn)
            else:
                board[nr][nc].fires += 1
                board[nr][nc].turn = turn
    return visits

def go_ice(board, x, y, turn):
    q = [(x, y, 0)]
    visited = [[False for _ in range(N)] for __ in range(N)]
    visited[x][y] = True
    dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
    visits = []
    while q:
        r, c, cnt = q.pop()
        if cnt == 1:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if oob(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            q.append((nr, nc, cnt+1))
            visited[nr][nc] = True
            visits.append((nr, nc))
            if board[nr][nc] == 0:
                board[nr][nc] = data(ices=1, turn=turn)
            else:
                board[nr][nc].ices += 1
                board[nr][nc].turn = turn
    return visits

def oob(r, c):
    return not (0 <= r < N and 0 <= c < N)

n=3
m=2
fires = [[1, 1]]
ices = [[3, 3]]
res = solution(n, m, fires, ices, )
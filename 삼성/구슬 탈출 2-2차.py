from collections import deque


def bfs(rr, rc, br, bc):
    Q = deque()
    Q.append(Bead(rr, rc, br, bc, 0))
    visited = [[[[False] * m for _ in range(n)]
                for _ in range(m)] for _ in range(n)]
    visited[rr][rc][br][bc] = True

    ret = -1
    while Q:
        cur = Q.popleft()

        if cur.cnt > 10:
            break
        if board[cur.rr][cur.rc] == 'O' and board[cur.br][cur.bc] != 'O':
            ret = cur.cnt
            break

        for i in range(4):
            next_rr, next_rc, next_br, next_bc = cur.rr, cur.rc, cur.br, cur.bc

            while board[next_rr][next_rc] != '#' and board[next_rr][next_rc] != 'O':
                next_rr += dr[i]
                next_rc += dc[i]

            while board[next_br][next_bc] != '#' and board[next_br][next_bc] != 'O':
                next_br += dr[i]
                next_bc += dc[i]

            if board[next_rr][next_rc] == '#':
                next_rr -= dr[i]
                next_rc -= dc[i]
            if board[next_br][next_bc] == '#':
                next_br -= dr[i]
                next_bc -= dc[i]

            if (next_rr, next_rc) == (next_br, next_bc):
                if board[next_rr][next_rc] != 'O':

                    red_dist = abs(next_rr - cur.rr) + abs(next_rc - cur.rc)
                    blue_dist = abs(next_br - cur.br) + abs(next_bc - cur.bc)

                    if red_dist > blue_dist:
                        next_rr -= dr[i]
                        next_rc -= dc[i]
                    else:
                        next_br -= dr[i]
                        next_bc -= dc[i]

            if not visited[next_rr][next_rc][next_br][next_bc]:
                visited[next_rr][next_rc][next_br][next_bc] = True
                Q.append(Bead(next_rr, next_rc, next_br, next_bc, cur.cnt + 1))

    return ret


class Bead:
    def __init__(self, rr, rc, br, bc, cnt) -> None:
        self.rr = rr
        self.rc = rc
        self.br = br
        self.bc = bc
        self.cnt = cnt


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, m = map(int, input().split())
board = [input() for _ in range(n)]
rr, rc = -1, -1
br, bc = -1, -1
min_cnt = float('inf')

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rr, rc = i, j
        if board[i][j] == 'B':
            br, bc = i, j

ret = bfs(rr, rc, br, bc)
print(ret)

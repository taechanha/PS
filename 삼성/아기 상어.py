n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
time = 0


class Shark:
    def __init__(self, r, c, size):
        self.r, self.c = r, c
        self.size = size
        self.num_eaten = 0

    def hunt(self):
        global board, time
        candidates, moves = self.move()
        if candidates == -1:
            return -1
        try:
            r, c = sorted(candidates, key=lambda x: (x[0], x[1]))[0]
        except:
            print(candidates)
            exit()

        if moves == float('inf'):
            print("ERROR")

        time += moves
        self.r, self.c = r, c
        board[r][c] = 0
        self.num_eaten += 1
        if self.num_eaten == self.size:
            self.size += 1
            self.num_eaten = 0

    def move(self):
        global board, dr, dc
        r, c = self.r, self.c
        Q = [(r, c)]
        dist = dict()
        dist[(r, c)] = 0
        shortest_dist = float('inf')
        candidates = []
        while Q:
            r, c = Q.pop(0)

            if board[r][c] != 0 and board[r][c] < self.size:
                if shortest_dist >= dist[(r, c)]: # 실수 1
                    shortest_dist = dist[(r, c)]
                    candidates.append((r, c))
            if dist[(r, c)] >= shortest_dist:
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                if (nr, nc) in dist:
                    continue
                if board[nr][nc] > self.size:
                    continue
                Q.append((nr, nc))
                dist[(nr, nc)] = dist[(r, c)] + 1

        return [candidates or -1, shortest_dist]


# 상어 초기화
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            shark = Shark(i, j, 2)

while True:
    # 상어 사냥
    ret = shark.hunt()
    
    # for row in board:
    #     print(row)
    # print(time)
    # exit()

    # 종료 조건
    if ret == -1:
        break


print(time)
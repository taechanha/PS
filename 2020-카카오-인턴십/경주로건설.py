class Car:
    def __init__(self, r, c, dir) -> None:
        self.r = r
        self.c = c
        self.dir = dir

    def move(self, r, c, nr, nc):
        cost = 100
        # self.r = nr
        # self.c = nc
        next_dir = self.get_dir(r, c, nr, nc)
        if self.dir != next_dir:
            if self.dir != 'init':
                cost += 500
            # self.dir = next_dir
        return cost

    def get_dir(self, r, c, nr, nc):
        if nc == c + 1:
            return 'r'
        elif nc == c - 1:
            return 'l'
        elif nr == r - 1:
            return 'u'
        elif nr == r + 1:
            return 'd'
        else:
            return self.dir


def out_of_bound(r, c):
    return not (0 <= r < n and 0 <= c < n)


def dfs(r, c, board):
    car = Car(r, c, 'init')
    queue = [car]
    visited = [(r, c)]
    dist = [[float('inf')] * n for _ in range(n)]
    dist[r][c] = 0
    while queue:
        car = queue.pop(0)
        if (car.r, car.c) == (n-1, n-1):
            return dist[-1][-1]
        # cand.append()
        for i in range(4):
            nr = car.r + dr[i]
            nc = car.c + dc[i]
            if out_of_bound(nr, nc):
                continue
            if board[nr][nc] == 1:
                continue
            # if (nr, nc) in visited:
                # continue
            curr_dist = car.move(car.r, car.c, nr, nc)
            if dist[nr][nc] > curr_dist + dist[car.r][car.c]:
                dist[nr][nc] = curr_dist + dist[car.r][car.c]
                queue.append(Car(nr, nc, car.get_dir(car.r, car.c, nr, nc)))
                visited.append((nr, nc))
    # print(dist)
    # print(visited)
    return dist[-1][-1]


def solution(board):
    global n, dr, dc
    n = len(board)
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    res1 = dfs(0, 0, board)
    # 우좌하상
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    res2 = dfs(0, 0, board)

    print(res1, res2)
    return min(res1, res2)


# board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# board = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [
    # 0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
# board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
# board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0],
#  [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
# board = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [
# 0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]


# 아래 케이스 딱 하나만 틀림. 이유 분석하자.
board = [[0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
         [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]]

res = solution(board)
print(res)

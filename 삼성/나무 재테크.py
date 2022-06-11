import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
trees = [list(map(int, input().split())) for _ in range(m)]
dr, dc = [-1, -1, -1, 0, 1, 1,  1, 0], [-1,  0,  1, 1, 1, 0, -1, -1]


class Cell:
    def __init__(self, nourishment, trees):
        self.nourishment = nourishment
        self.trees = trees

    def spring(self):
        # self.trees.sort(key=lambda x: x[0]) # 개선 1
        for i in range(len(self.trees)):
            if self.nourishment >= self.trees[i][0]:
                self.nourishment -= self.trees[i][0]
                self.trees[i][0] += 1
            else:
                self.trees[i][1] = 0

    def summer(self):
        len_trees = len(self.trees)
        # trees_to_be_deleted = set() # 개선 2
        check = None
        for i in range(len_trees):
            if self.trees[i][1] == 0:
                if check == None:
                    check = i
                self.nourishment += self.trees[i][0] // 2
                # trees_to_be_deleted.add(i)

        if check == None:
            return
        for _ in range(check, len_trees):
            self.trees.pop()
        # self.trees = [self.trees[i]
        #               for i in range(len_trees) if i not in trees_to_be_deleted]


board = [[0] * n for _ in range(n)]
for x, y, z in trees:
    board[x-1][y-1] = Cell(5, [[z, 1]])

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = Cell(5, [])

while k > 0:
    k -= 1

    for r in range(n):
        for c in range(n):
            board[r][c].spring()

    # 여름
    for r in range(n):
        for c in range(n):
            board[r][c].summer()

    # 가을
    for r in range(n):
        for c in range(n):
            for tree in board[r][c].trees:
                if tree[0] % 5 != 0:
                    continue
                for i in range(8):
                    nr, nc = r + dr[i], c + dc[i]
                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    board[nr][nc].trees.insert(0, [1, 1])

            # 겨울
            board[r][c].nourishment += A[r][c]

trees = 0
for r in range(n):
    for c in range(n):
        trees += len(board[r][c].trees)

print(trees)

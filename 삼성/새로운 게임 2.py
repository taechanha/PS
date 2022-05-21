n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pieces = [list(map(lambda x: int(x)-1, input().split())) for _ in range(k)]

# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# 0: 흰  1: 빨  2: 파
maps = {0: 1, 1: 0,
        2: 3, 3: 2}
turns = 0

print(pieces)
while turns <= 1000:
    turns += 1

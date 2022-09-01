board = [list(map(int, input().split())) for _ in range(11)]

print(sum([row.count(0) for row in board]))

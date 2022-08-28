# 7:32 ~ 7:50

n, m = map(int, input().split())
board = [input() for _ in range(n)]
data = []

def find_words(n, m):
    data = []
    for r in range(n):
        accum = ""
        for c in range(m):
            if board[r][c] == '#':
                if len(accum) < 2:
                    continue
                data.append(accum)
                accum = ""
                continue
            accum += board[r][c]
        if len(accum) >= 2:
            data.append(accum)
    return data

# valid
# 1. row by row
for r in range(n):
    accum = ""
    for c in range(m):
        if board[r][c] == '#':
            if len(accum) >= 2:
                data.append(accum)
            accum = ""
            continue
        accum += board[r][c]
    if len(accum) >= 2:
        data.append(accum)
# 2. col by col
for c in range(m):
    accum = ""
    for r in range(n):
        if board[r][c] == '#':
            if len(accum) >= 2:
                data.append(accum)
            accum = ""
            continue
        accum += board[r][c]
    if len(accum) >= 2:
        data.append(accum)

data.sort()
print(data[0])

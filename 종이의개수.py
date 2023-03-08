def allSameColor(n, r, c):
    cnt_1, cnt0, cnt1 = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if board[i+r][j+c] == -1:
                cnt_1 += 1
            elif board[i+r][j+c] == 0:
                cnt0 += 1
            elif board[i+r][j+c] == 1:
                cnt1 += 1
    if cnt_1 == n*n:
        return -1
    elif cnt0 == n*n:
        return 0
    elif cnt1 == n*n:
        return 1
    return None


def find(n, r, c):
    if n == 1:
        colors[board[r][c]] += 1
        return

    # 모두 같은 색?
    ret = allSameColor(n, r, c)
    if ret in (-1, 0, 1):
        colors[ret] += 1
        return

    # 아니면, 9개로 분할
    div = n//3
    for i in range(3):  # row
        for j in range(3):  # col
            find(div, r+i*div, c+j*div)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
colors = {-1: 0, 0: 0, 1: 0}
find(n, 0, 0)

[print(colors[color]) for color in colors.keys()]

# 9:09 ~

n = t = int(input())
board = [[0] * 20 for _ in range(20)]


def is_gobang(k):
    global r, c
    cnt = 1
    gobang = False
    for i in range(20-1):
        if k == 0:
            if board[i][c] == board[i+1][c] and board[i][c] != 0:
                cnt += 1
            else:
                if cnt == 5:
                    gobang = True
                    break
                cnt = 1
        elif k == 1:
            if board[r][i] == board[r][i+1] and board[r][i] != 0:
                cnt += 1
            else:
                if cnt == 5:
                    gobang = True
                    break
                cnt = 1
    if gobang:
        return True

    if k == 2:
        # find base point
        r = r + c
        c = 0
        cnt = 1
        gobang = False
        for i in range(20-1):
            if not (0 <= r-i-1 < 20 and 0 <= c+i+1 < 20):
                break
            if board[r-i][c+i] == board[r-i-1][c+i+1] and board[r-i][c+i] != 0:
                cnt += 1
            else:
                if cnt == 5:
                    gobang = True
                    break
                cnt = 1
        if gobang:
            return True
    else:
        r = 0
        c = c - r
        cnt = 1
        gobang = False
        for i in range(20-1):
            if not (0 <= r+i+1 < 20 and 0 <= c+i+1 < 20):
                break
            if board[r+i][c+i] == board[r+i+1][c+i+1] and board[r+i][c+i] != 0:
                cnt += 1
            else:
                if cnt == 5:
                    gobang = True
                    break
                cnt = 1
    if gobang:
        return True

    return False


black = True
should_continue = True
ans = -1
while t:

    t -= 1

    r, c = map(lambda x: int(x)-1, input().split())

    if black:
        board[r][c] = 'B'
        black = False
    else:
        board[r][c] = 'W'
        black = True

    # 현재 놓은 위치에서 가능한 오목 방향으로 조사?
    # 1. 상하
    if not should_continue:
        continue
    ret = is_gobang(0)
    # 2. 좌우
    ret |= is_gobang(1)
    # 3. 10 5
    ret |= is_gobang(2)
    # 4. 2 7
    ret |= is_gobang(3)

    if ret:
        ans = n - t
        should_continue = False

print(ans)

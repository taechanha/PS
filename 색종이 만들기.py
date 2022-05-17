n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def is_all_equal(rs, re, cs, ce):
    total = re-rs
    cnt = 0
    rr, cc = None, None
    for r in range(rs, re):
        for c in range(cs, ce):
            cnt += board[r][c]
            if (rr, cc) == (None, None):
                rr, cc = r, c
    return total == cnt, board[rr][cc]


def dfs(row_start, row_end, col_start, col_end):
    global blue, white
    eq, BLUE = is_all_equal(row_start, row_end, col_start, col_end)
    if eq:
        if BLUE:
            blue += 1
        else:
            white += 1
        return
    if (row_end - row_start) == 1 or (col_end - col_start) == 1:
        BLUE = board[row_start][col_start]
        if BLUE:
            blue += 1
        else:
            white += 1
        return

    dfs(row_start, row_end//2, col_start, col_end//2)
    dfs(row_start, row_end//2, col_start//2, col_end)
    dfs(row_start//2, row_end, col_start, col_end//2)
    dfs(row_start//2, row_end, col_start//2, col_end)


blue, white = 0, 0
dfs(n, n, n, n)
print(blue, "\n", white)

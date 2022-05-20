# 9:54 ~

# Yes No

R, C, K = map(int, input().split())
board = [list(input()) for _ in range(R)]


def dfs(r, c, ccw_n, cw_n, visited):
    # 출구에 다다르면 종료
    if not (0 <= r < R and 0 <= c < C):
        return False
    if (r, c) == (R-1, C-1):
        return True
    if (r, c, ccw_n, cw_n) in visited:
        return False

    # 바닥에 적혀있는 화살표에 맞춰 그대로 이동
    bool = False

    visited[(r, c, ccw_n, cw_n)] = True
    if (r, c, ccw_n, cw_n) == (1, 1, 1, 0):
        print("")

    arrow = board[r][c]
    dr, dc = move[arrow]
    bool |= dfs(r+dr, c+dc, ccw_n, cw_n, visited)
    if bool:
        return bool

    # 화살표를 반시계로 회전한 다음 이동
    if ccw_n > 0:
        arrow = board[r][c]
        board[r][c] = ccw[arrow]
        bool |= dfs(r, c, ccw_n-1, cw_n, visited)
        board[r][c] = cw[arrow]
        if bool:
            return bool

    # 화살표를 시계로 회전한 다음 이동
    if cw_n > 0:
        arrow = board[r][c]
        board[r][c] = cw[arrow]
        bool |= dfs(r, c, ccw_n, cw_n-1, visited)
        board[r][c] = ccw[arrow]
        if bool:
            return bool

    return bool


move = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

ccw = {
    'R': 'U',
    'U': 'L',
    'L': 'D',
    'D': 'R'
}

cw = {
    'R': 'D',
    'D': 'L',
    'L': 'U',
    'U': 'R'
}

visited = {}
print("Yes") if dfs(0, 0, K, K, visited) else print("No")

for k, v in visited.items():
    print(k)

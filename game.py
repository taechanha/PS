# 3 7
# 3942178
# 1234567
# 9123532
global tmp
tmp = []


def dfs(i, j, cnt):
    if cnt >= n * m:
        print(-1)
        exit()
    if i >= n or i < 0 or j >= m or j < 0 or board[i][j] == 'H':
        return cnt
    else:
        next = int(board[i][j])
        cnt1 = max(dfs(i + next, j, cnt + 1), dfs(i - next, j, cnt + 1))
        cnt2 = max(dfs(i, j + next, cnt + 1), dfs(i, j - next, cnt + 1))
        return max(cnt1, cnt2)


def main():
    global n, m
    global board
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    cnt = 0
    if n == m and n == 1:
        print(1)
        return
    print(dfs(0, 0, cnt))
    # print(tmp)


if __name__ == '__main__':
    main()

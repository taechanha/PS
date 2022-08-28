n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tmp = []


def dfs(i, j):
    if i >= n or j >= m:
        return
    if i == j:
        tmp.append(i)
    else:
        for i in range(i, n):
            for j in range(j, m):
                if board[i][j] == 1:
                    dfs(i + 1, j)
                    dfs(i, j + 1)


dfs(0, 0)

print(tmp)

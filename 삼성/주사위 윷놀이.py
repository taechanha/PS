board = [1, 2, 3, 4, 5, 6]
dice = [1, 2, 3]
n = len(board)
m = len(dice)


def dfs(i, chosen):
    if i >= n:
        print(chosen)
        return
    for k in range(m):
        chosen += board[i]
        dfs(i+dice[k], chosen)
        chosen -= board[i]


dfs(0, 0)

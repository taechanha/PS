def dfs(n, m, chosen):
    if m == 0:
        print(' '.join(chosen))
    else:
        for i in range(1, n + 1):
            if str(i) not in chosen:
                chosen += str(i)
                dfs(n, m - 1, chosen)
                chosen = chosen[:-1]


n, m = map(int, input().split())
dfs(n, m, "")

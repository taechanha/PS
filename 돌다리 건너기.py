# 6:30 ~
from functools import lru_cache

data = input()
angel = input()
devil = input()
n = len(angel)
m = len(data)

# STEP BY STEP
@lru_cache(None)
def dfs(k, i, turn):
    if k == m:
        return 1
    if i >= n:
        return 0
    if turn:
        # angel turn: i
        up = 0
        for ii in range(i, n):
            if angel[ii] == data[k]:
                up += dfs(k+1, ii+1, 0)
        return up
    else:
        # devil turn: j
        down = 0
        for ii in range(i, n):
            if devil[ii] == data[k]:
                down += dfs(k+1, ii+1, 1)
        return down

res = dfs(0, 0, 0) + dfs(0, 0, 1)
print(res)

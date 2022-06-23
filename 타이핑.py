import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)


@lru_cache(None)
def dfs(i, capslock_on):
    if i == n:
        return 0

    if string[i].isupper():
        if capslock_on:
            return dfs(i+1, capslock_on)
        else:
            return min(dfs(i+1, True) + 1, dfs(i+1, False) + 1)
    else:
        if capslock_on:
            return min(dfs(i+1, True) + 1, dfs(i+1, False) + 1)
        else:
            return dfs(i+1, capslock_on)


# iLoveINHA
string = input()
n = len(string)
res = dfs(0, False)
print(res + n)

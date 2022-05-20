# 회전과 이동에 대한 DFS?
from functools import cache, lru_cache
import sys
sys.setrecursionlimit(26000)


def rotate_cw(key):
    n = len(key)
    m = len(key[0])
    new = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            new[c][n-1-r] = key[r][c]
    return new


def is_unlocked(key, lock):
    n = len(key)
    m = len(key[0])
    for i in range(n):
        for j in range(m):
            if key[i][j] + lock[i][j] != 1:
                return False
    return True


def move(key, op):
    """
    op: 0 -> 위   | 1 -> 오른쪽
        2 -> 아래  | 3 -> 왼쪽
    """
    n = len(key)
    m = len(key[0])
    new = [row[:] for row in key]
    if op == 2:
        for i in range(n-1, -1, -1):
            for j in range(m):
                if i == n-1:
                    new[i][j] = 0
                else:
                    new[i+1][j] = new[i][j]
                    new[i][j] = 0
        return new
    else:
        # op == 1 or 2 or 3
        if op == 1:
            new = rotate_cw(new)
        elif op == 3:
            new = rotate_cw(rotate_cw(new))
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if new[i][j] == 1:
                        new[i][j] = 0
                else:
                    new[i-1][j] = new[i][j]
                    new[i][j] = 0
        return new


def termination_condition(key):
    if sum([sum(row) for row in key]) == 0:
        return True
    return False


def dfs(key, lock, rotate_count, move_count):
    if is_unlocked(key, lock):
        return True
    if termination_condition(key):
        return False
    # if rotate_count == 0:
    #     return False
    # if move_count == 0:
    #     return False
    # move or rotate
    if (str(key), str(lock), rotate_count, move_count) in memo:
        return memo[(str(key), str(lock), rotate_count, move_count)]
    memo[(str(key), str(lock), rotate_count, move_count)] = dfs(rotate_cw(key), lock, rotate_count-1, m) \
        or dfs(move(key, 0), lock, 4, m-1) \
        or dfs(move(key, 1), lock, 4, m-1) \
        or dfs(move(key, 2), lock, 4, m-1) \
        or dfs(move(key, 3), lock, 4, m-1)
    return memo[(str(key), str(lock), rotate_count, move_count)]


def solution(key, lock):
    global m, memo
    N = len(lock)
    M = len(lock[0])
    n = len(key)
    m = len(key[0])
    memo = dict()
    for i in range(N-n+1):
        for j in range(M-m+1):
            new_lock = [[0] * 3 for _ in range(3)]
            for k in range(3):
                for o in range(3):
                    new_lock[k][o] = lock[i+k][j+o]
            # key.shape == new_lock.shape
            if dfs(key, new_lock, 4, m) == True:
                return True
    return False


key = [[0, 0, 0],
       [1, 0, 0],
       [0, 1, 1]]

lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

res = solution(key, lock)
print(res)

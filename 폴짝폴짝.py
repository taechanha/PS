# 5:51 ~

# -> 최단거리는 그냥 bfs로 푼다고 생각하자..
from functools import lru_cache

n = int(input())
board = [None] + list(map(int, input().split()))
s, e = map(int, input().split())

@lru_cache(None) 
def dfs(i, jumps):
    if i < 1:
        return float('inf')
    if i > e:
        return float('inf')
    if i == e:
        return jumps
    case1 = float('inf')
    n = board[i]
    s, j = 0, 1
    while s < 10_000:
        s = j * n
        j += 1
        ret = dfs(i+s, jumps+1)
        if ret == float('inf'):
            break
        case1 = min(case1, ret)
    return case1


res = dfs(s, 0)
print(-1) if res == float('inf') else print(res)
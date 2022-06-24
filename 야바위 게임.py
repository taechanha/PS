# 5:21 ~ 5:31
from collections import defaultdict


def dfs(start):
    stack = [(start, 0)]
    visited = [[False] * times for _ in range(n+1)]
    visited[start][0] = True
    answer = []
    while stack:
        curr, t = stack.pop()
        if t == times:
            answer.append(curr)
            continue
        for neigh in G[curr]:
            if visited[neigh][t]:
                continue
            stack.append((neigh, t+1))
            visited[neigh][t] = True
    return answer


n, m, start, times = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

answer = dfs(start)
print(-1) if not answer else print(*sorted(answer))

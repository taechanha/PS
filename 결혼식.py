# 5:05 ~

# 1에서 시작해서 depth 2까지의 노드 리스트
from collections import defaultdict


def dfs(s):
    stack = [(s, 0)]
    visited = [False] * (n+1)
    visited[s] = True
    while stack:
        curr, dist = stack.pop()
        if dist == 2:
            continue
        for neigh in G[curr]:
            if visited[neigh]:
                continue
            stack.append((neigh, dist+1))
            visited[neigh] = True
    return visited


n = int(input())
m = int(input())
G = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = dfs(1)
answer = sum(visited)-1
print(answer)

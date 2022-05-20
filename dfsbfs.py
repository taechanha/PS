from collections import defaultdict
from collections import deque


def dfs(G, s):
    stack = [s]
    visited = [False] * (n + 1)
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = True
            print(curr)
            for neighbor in sorted(G[curr], reverse=True):
                stack.append(neighbor)


def bfs(G, s):
    q = deque([s])
    visited = []
    visited.append(s)
    while q:
        curr = q.popleft()
        print(curr)
        for neighbor in sorted(G[curr]):
            if neighbor not in visited:
                visited.append(neighbor)
                q.append(neighbor)


n, m, v = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    s, e = map(int, input().split())
    G[s].append(e)
    G[e].append(s)

dfs(G, v)
bfs(G, v)

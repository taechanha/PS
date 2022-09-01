from collections import defaultdict, deque


def bfs(s):
    Q = deque([s])
    visited = [True] + [False] * (n-1)
    while Q:
        curr = Q.popleft()
        for neigh in G[curr].keys():
            if visited[neigh]:
                continue
            Q.append(neigh)
            visited[neigh] = True
    return visited


n = int(input())
m = int(input())
G = defaultdict(dict)
for U in range(n):
    Vs = list(map(int, input().split()))
    for V, e in enumerate(Vs):
        if e == 0:
            continue
        G[U][V] = 0
        G[V][U] = 0
target = list(map(lambda x: int(x)-1, input().split()))

visited = bfs(target[0])

cnt = 0
for t in target:
    if visited[t]:
        cnt += 1

print("YES") if cnt == len(target) else print("NO")

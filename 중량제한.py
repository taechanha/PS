import heapq
from collections import defaultdict


def dijkstra(start):
    global n
    q = []
    heapq.heappush(q, (0, start))
    dist = [float('inf')] * n
    dist[start] = 0

    while q:
        weight, curr = heapq.heappop(q)
        if dist[curr] < weight:
            continue
        for neigh_wt, neigh in G[curr]:
            cost = weight + neigh_wt
            if dist[neigh] > cost:
                dist[neigh] = cost
                heapq.heappush(q, (cost, neigh))
    return dist

# 3 3
# 1 2 2
# 3 1 3
# 2 3 2
# 1 3


n, m = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    u, v, w = map(lambda x: int(x), input().split())
    G[u-1].append((w, v-1))
    G[v-1].append((w, u-1))
start, end = map(lambda x: int(x)-1, input().split())

print(G)

dist = dijkstra(start)
print(dist)

# 10:10 ~ 10:34

from collections import defaultdict
import heapq


def dijkstra(s, t):
    # init dist
    INF = float('inf')
    dist = [INF for _ in range(n+1)]
    dist[s] = 0
    # init pq
    pq = [(s, 0)]

    while pq:
        curr_node, curr_dist = heapq.heappop(pq)
        # if curr_node == t:                      ##### 더 좋은 경로로 업데이트 될 수 있잖아~~~~~~~~~
        #     return curr_dist
        for neighbor_node, neighbor_dist in G[curr_node]:
            if dist[neighbor_node] > curr_dist + neighbor_dist:
                dist[neighbor_node] = curr_dist + neighbor_dist
                heapq.heappush(pq, (neighbor_node, dist[neighbor_node]))
    return dist[t]


n, m = map(int, input().split())

# construct graph
G = defaultdict(list)
for _ in range(m):
    u, v, weight = map(int, input().split())
    G[u].append((v, weight))
    G[v].append((u, weight))

# start, target
s, t = map(int, input().split())

# get shortest distance from s to t
ret = dijkstra(s, t)
print(ret)

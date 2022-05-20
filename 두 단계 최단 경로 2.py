# 10:43 ~ 12:13 (불필요한 커팅)

import sys
import heapq
input = sys.stdin.readline

def dijkstra(s):
    INF = 987654321
    dist = [INF for _ in range(n)]
    dist[s] = 0
    pq = [(s, 0)]
    while pq:
        curr, curr_dist = heapq.heappop(pq)
        if curr_dist > dist[curr]:
            continue
        for neighbor, neighbor_dist in G[curr]:
            if dist[neighbor] > curr_dist + neighbor_dist:
                dist[neighbor] = curr_dist + neighbor_dist
                heapq.heappush(pq, (neighbor, dist[neighbor]))
    return dist

n, m = map(int, input().split())
G = [[] for _ in range(n)]

# construct graph
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u-1].append((v-1, w))
    G[v-1].append((u-1, w))

s, t = map(lambda x: int(x)-1, input().split())
k = int(input())
p = list(map(lambda x: int(x)-1, input().split()))

# get shortest distance from X to all
dist1 = []
dist2 = []
dist1 = dijkstra(s)
dist2 = dijkstra(t)

# s -> p_i -> t
INF = 987654321
min_dist = INF
for i in range(k):

    to_middle = dist1[p[i]]
    to_target = dist2[p[i]]

    min_dist = min(min_dist, to_middle + to_target)

if min_dist == 0:
    print(-1)
else:
    print(min_dist)

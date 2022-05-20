import heapq
from collections import defaultdict


def dijkstra(G, start):
    # init dist
    dist = [INF for _ in range(n)]
    dist[start] = 0
    # init pq
    pq = [(start, 0)]

    while pq:
        curr_node, curr_dist = heapq.heappop(pq)
        for neighbor_node, neighbor_dist in G[curr_node]:
            if dist[curr_node] > curr_dist + neighbor_dist:
                dist[curr_node] = curr_dist + neighbor_dist
                heapq.heappush(pq, (curr_node, dist[curr_node]))


def solution(n, s, a, b, fares):
    G = defaultdict(list)
    for s, e, cost in fares:
        G[s].append((e, cost))
        G[e].append((s, cost))

    answer = 0
    return answer


INF = float('inf')
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
    5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
# res = solution(n, s, a, b, fares)
# print(res)

# 그냥 계속 '도착지'만 바꿔주면 될듯?


# 그래프 초기화
# 다익스트라

# 완전 탐색?
# 1. 모든 경로를 합승해서 가는 경우  -> 둘을 하나로 보고 다익스트라(한 도착지 도착 후 다른 지점을 도착지로 다시 돌아야함. 생각해보면)
# 2. 마지막 한 경로만 따로 가는 경우 -> 마지막 이전 까지 둘을 하나로 보고 다익스트라 & 그 위치에서 각자 다익 & 합산
# 3. 마지막 두 경로만 따로 가는 경우
#    ...
# n. 첫 지점을 제외하고 모두 따로 가는 경우 -> 각자 다익(도착지 다름) & 합산

# 1. A를 목적으로 갔다가, A에 도착하면 B를 목적으로 출발 -> 그 때 까지의 비용 합산


# n. 각자 다른 목적지를 가지고 다익스트라 -> 비용 합산


# Floyd - warshal

def solution(n, s, a, b, fares):
    INF = float('inf')
    # init graph
    d = [[INF if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

    # set graph
    for fare in fares:
        u, v, cost = fare
        if d[u][v] > cost:
            d[u][v] = cost
        if d[v][u] > cost:
            d[v][u] = cost
    # relax
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    # for i in range(1, n+1):
    #     print(d[i])

    min_dist = INF
    for k in range(1, n+1):
        min_dist = min(min_dist, (d[s][k] + d[k][a] + d[k][b]))
    return min_dist


res = solution(n, s, a, b, fares)
print(res)

# 이렇게 했어도 되었을듯?
# min_dist = INF
# for k in range(1, n+1):
#     min_dist = min(min_dist, (diikstra(s, k) + diikstra(k, a) + diikstra(k, b)))
import heapq
import sys
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    global distance
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

---------------------------------------------------------------------------------------------------------------------------------------------------------
# 더 단순하게 구현해보자..
# if distance[now] < dist 부분이 진짜 필요한가?
# distance[now]는 초기에 INF로 초기화되어 있음
# dist는 한 번 loop through 했을 때 start로 부터 도달할 수 있는 정점들이 pq에 start로 부터의 dist와 함께 저장될 것임
# 46 라인이 뜻하는 바는 start로 부터 now까지의 dist가 현재 now까지의 거리보다 크다면! 임. 그니까 이 경우는 그 경로를 밟으면 최단 경로로 가지 못함. 
# (이 조건문에 부합하지 않는 다른 '지름길'은 없다; 음수 cost는 가정하지 않는다. 더 짧은 경로의 길이가 존재한다면 distance[now] > dist일 것이고, 그러면 그 아래 로직을 진행하면 된다.)

# 즉, 위와 같이 코드를 작성하면 현재 정점의 이웃 정점들을 탐색하는 루프에 불필요하게 진입할 일이 없다.

# 근데 그 손해가 유의미한가?? 목적이 뭐지? 코테. 코테에서는 세세한 차이로 timeout 되지 않음. 깔끔한 게 더 중요. 애초에 깔끔하게 짰으면 가지치기는 더 쉬웠을 것. 처음부터 가지치기 하려고 하면 복잡함


def dijkstra(G, start):
    #init dist
    dist = [INF for _ in range(n)]
    dist[start] = 0
    #init pq
    pq = [ (start, 0) ]
    
    while pq:
        curr_node, curr_dist = heapq.heappop(pq)
        if distance[curr_node] < curr_dist:
            continue
        for neighbor_node, neighbor_dist in G[curr_node]:
            if dist[neighbor_node] > curr_dist + neighbor_dist:
                dist[neighbor_node] = curr_dist + neighbor_dist
                heapq.heappush(pq, (neighbor_node, dist[neighbor_node]))
    

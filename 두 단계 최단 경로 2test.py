

n, m = map(int, input().split())

INF = float('inf')
dist = [[INF] * n for _ in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    dist[u-1][v-1] = w
    dist[v-1][u-1] = w

for i in range(n):
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

s, t = map(lambda x: int(x)-1, input().split())
_ = int(input())
p = list(map(lambda x: int(x)-1, input().split()))


INF = float('inf')
min_dist = INF
for i in range(_):
    to_middle = dist[s][p[i]]
    to_target = dist[p[i]][t]
    if to_middle == 0:
        to_middle = INF
    if to_target == 0:
        to_target = INF
    min_dist = min(min_dist, to_middle + to_target)

if min_dist == INF:
    print(-1)
else:
    print(min_dist)

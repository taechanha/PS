n, m = map(int, input().split())
INF = float('inf')
graph = [[INF] * (n) for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1
    graph[v-1][u-1] = 1
for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_kevin = INF
ans = None
for i, row in enumerate(graph):
    s = sum(row)
    if min_kevin > s:
        min_kevin = s
        ans = i+1

print(ans)

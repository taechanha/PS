# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1
from collections import defaultdict

v = int(input())
G = defaultdict(list)

INF = float('inf')
G = [[INF] * (v+1) for _ in range(v+1)]

# graph setting
for _ in range(v):
    si = list(map(int, input().split()))
    start = si[0]
    ends = si[1:-1]
    for i in range(0, len(ends), 2):
        end, dist = ends[i], ends[i+1]
        G[start][end] = dist

# get farthest distance
# floyd warshall
for k in range(v+1):
    for i in range(v+1):
        for j in range(v+1):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

print(G)

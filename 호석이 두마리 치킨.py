# 11:57 ~ 1:00

n, m = map(int, input().split())


def bfs(s):
    global G
    Q = [s]
    dist = [None for _ in range(n)]
    dist[s] = 0
    while Q:
        curr = Q.pop(0)
        for neighbor in G[curr]:
            if dist[neighbor] != None:
                continue
            Q.append(neighbor)
            dist[neighbor] = dist[curr] + 1
    return dist


# construct graph
G = [[] * n for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)

# 치킨집 선정
# 각 건물에서 가장 가까운 치킨집까지의 거리
dist = []
for i in range(n):
    dist.append(bfs(i))

# for row in dist:
    # print(row)

min_cnt = float('inf')
for i in range(n-1):
    for j in range(i+1, n):
        # chicken store: i, j
        s = set(range(n)).difference({i, j})
        cnt = 0
        for each in s:
            cnt += min(dist[each][i], dist[each][j]) * 2

        if min_cnt > cnt:
            min_cnt = cnt
            ans = i, j

print(*map(lambda x: int(x)+1, ans), min_cnt)

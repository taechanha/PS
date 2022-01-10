def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
        rank[x] += rank[y]
    else:
        parent[x] = y
        rank[y] += rank[x]


class Edge:
    def __init__(self, a, b, c):
        self.node = [a, b]
        self.dist = c


n = int(input())
m = int(input())
parent = [_ for _ in range(100001)]
rank = [_ for _ in range(100001)]
wsum = 0
v = []

for _ in range(m):
    a, b, c = map(int, input().split())
    v.append(Edge(a, b, c))

v.sort(key=lambda x: x.dist)

for i in range(len(v)):
    if find(v[i].node[0]) != find(v[i].node[1]):
        wsum += v[i].dist
        union(v[i].node[0], v[i].node[1])

print(wsum)

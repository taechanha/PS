n, m = map(int, input().split())
parent = [x for x in range(n)]
rank = [1 for _ in range(n)]


def find(x):
    if x == parent[x]:
        return x

    y = find(parent[x])
    parent[x] = y
    return parent[x]


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


for _ in range(m):
    u, v = map(int, input().split())
    union(u-1, v-1)

ans = set()
for i in range(n):
    ans.add(find(i))

print(len(ans))

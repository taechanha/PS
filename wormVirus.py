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


n = int(input())
m = int(input())

parent = [x for x in range(n + 1)]
rank = [1 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

cnt = 0

for i in range(2, n):
    if find(i) == 1:
        cnt += 1

print(cnt)
print(parent)

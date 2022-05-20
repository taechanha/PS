from collections import defaultdict


def dfs(G, s, count):
    if count == 4:
        print(1)
        exit()
    else:
        for neighbor in G[s]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dfs(G, neighbor, count + 1)
                visited[neighbor] = False


n, m = map(int, input().split())
G = defaultdict(list)

# init G
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(n):
    # start dfs from 0, mark 0 as visited
    visited = [False] * (n)
    visited[i] = True
    # if conditions satisfied, print 1 and exit
    dfs(G, i, 0)

# else, print 0
print(0)

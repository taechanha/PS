from collections import defaultdict, deque
import sys
input = sys.stdin.readline

# def dfs(G, start):
#     S = [start]
#     prev = [0] * (n + 1)
#     prev[start] = start

#     while S:
#         curr_v = S.pop()

#         for neigh_v in G[curr_v]:
#             num_of_com_from[curr_v] += 1
#             prev[neigh_v] = curr_v
#             S.append(neigh_v)

#     return prev


# def dfs(G, s, count):
#     if not G[s]:
#         counter[s] = count + 1
#     else:
#         for neigh_v in G[s]:
#             dfs(G, neigh_v, count + 1)

def bfs(G, s):
    q = deque([s])
    visited = [0] * (n + 1)
    visited[s] = True

    count = 0
    while q:
        curr_v = q.popleft()
        count += 1

        for neigh_v in G[curr_v]:
            if not visited[neigh_v]:
                visited[neigh_v] = True
                q.append(neigh_v)

    return count


n, m = map(int, input().split())
G = defaultdict(list)
visited = [0] * (n + 1)
counter = [0] * (n + 1)

# set G
for _ in range(m):
    v1, v2 = map(int, input().split())
    G[v2].append(v1)  # put in reverse order to dfs easier


for i in range(1, n + 1):
    counter[i] = bfs(G, i)

max_count = max(counter)
for i in range(1, n + 1):
    if counter[i] == max_count:
        print(i, end=' ')

# print max hackable computer FROM

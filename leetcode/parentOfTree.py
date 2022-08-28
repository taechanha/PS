
# n = int(input())
# parent = [_ for _ in range(n + 1)]

# is_in_tree = [False] * (n + 1)  # represent if node gets in tree
# is_in_tree[1] = True

# # 1. 1 6
# # check one of them is 1: if yes, op1) put the other one as a son of 1 and put the other in tree
# #                  if no,  check if one of them is in tree:       if yes, op1)
# #                                                                 if no, NOT MAKE SENSE

# # 7
# # 1 6
# # 6 3
# # 3 5
# # 4 1
# # 2 4
# # 4 7

# input_list = []
# for _ in range(n - 1):
#     node1, node2 = map(int, input().split())
#     input_list.append([node1, node2])
# print(input_list)
# input_list.sort(key=lambda x: (x[0], x[1]))
# print(input_list)

# for i in range(n - 1):
#     # node1, node2 = map(int, input().split())
#     node1, node2 = input_list[i]

#     if is_in_tree[node1] == True:
#         parent[node2] = node1
#         is_in_tree[node2] = True

#     elif is_in_tree[node2] == True:
#         parent[node1] = node2
#         is_in_tree[node1] = True

# for i in range(2, n + 1):
#     # parent[i] = i's parent
#     print(parent[i])

# --------------------------------------------

from collections import defaultdict, deque


def bfs(G, s):
    q = deque([s])
    visited[s] = True  # X
    # parent[s] = (s or True or whatever except 0)
    while q:
        curr_node = q.popleft()

        for neigh_node in G[curr_node]:
            if visited[neigh_node] == False:   # parent[neigh_node] == 0:
                visited[neigh_node] = True     # X
                parent[neigh_node] = curr_node
                q.append(neigh_node)


n = int(input())
visited = [False] * (n + 1)
parent = [0] * (n + 1)

G = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    G[node1].append(node2)
    G[node2].append(node1)


bfs(G, 1)

for i in range(2, n + 1):  # for i in parent[2:]:
    print(parent[i])

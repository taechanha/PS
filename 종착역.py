from collections import deque
from collections import defaultdict


def bfs(G, s):
    q = deque([s])
    visited = []
    count_passenger = [0] * n
    count_passenger[1] = passenger[1]

    print(count_passenger)
    while q:
        curr = q.popleft()

        for neighbor in G[curr]:
            q.append(neighbor)
            count_passenger[neighbor] = count_passenger[curr] + \
                passenger[neighbor]

    temp = []
    temp_max = max(count_passenger)
    for i in range(len(count_passenger)):
        if count_passenger[i] == temp_max:
            temp.append([i, temp_max])
    temp.sort(key=lambda x: (-x[0]))
    return temp[0]


passenger = [0, 1, 1, 1, 1, 1, 1]
train = [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6]]

n = len(passenger)

G = defaultdict(list)

for each in train:
    G[each[0]].append(each[1])

print(bfs(G, 1))

# todo 1: adj list - DONE
from collections import defaultdict
from collections import deque

n, m = map(int, input().split())
adj_list = defaultdict(list)
in_degree = [0] * (n + 1)
q = deque()
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    in_degree[b] += 1


for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)


# todo 2: indegree pop
for i in range(n):
    now = q.popleft()
    ans.append(now)

    for i in range(len(adj_list[now])):
        next = adj_list[now][i]
        in_degree[next] -= 1
        # todo 3: if indegree == 0: insert to queue
        if in_degree[next] == 0:
            q.append(next)

print(ans)

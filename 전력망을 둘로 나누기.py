# 2:43 ~ 3:01
from collections import defaultdict


def dfs(s):
    global G, n, visited
    S = [s]
    visited[s] = True
    cnt = 0
    while S:
        curr = S.pop()
        for neigh in G[curr]:
            if visited[neigh]:
                continue
            S.append(neigh)
            visited[neigh] = True
            cnt += 1
    return cnt


def solution(n, wires):
    global G, visited
    min_diff = float('inf')
    # 1. 그래프 구성
    for i in range(n):
        G = defaultdict(list)
        visited = [False] * n
        for e, (u, v) in enumerate(wires):
            u, v = u-1, v-1
            if e == i:
                continue
            G[u].append(v)
            G[v].append(u)
        # print(f"{i}: ", G)
        # 2. 간선 하나씩 삭제하면서, 나눠진 두 개의 그래프의 노드 개수 구하기
        networks = [0, 0]
        flag = 0
        for curr in range(n):
            if visited[curr]:
                continue
            cnt = dfs(curr)
            if cnt == 0:
                continue
            networks[flag] = cnt
            flag = 1
        # print(f"{i}: ", networks)
        diff = abs(networks[0]-networks[1])
        min_diff = min(min_diff, diff)

    # 3. 최소 노드 개수 차이 리턴
    return min_diff


n = 7
wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
# n = 4
# wires = [[1, 2], [2, 3], [3, 4]]
# n = 9
# wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
res = solution(n, wires)
print(res)

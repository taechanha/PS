# 8:25 ~ 9:18

from itertools import combinations as C
from collections import defaultdict

n = int(input())
population = list(map(int, input().split()))
G = defaultdict(list)
for u in range(n):
    vs = list(map(lambda x: int(x)-1, input().split()))
    G[u] += vs[1:]
    for v in vs[1:]:
        G[v] += [u]


def dfs(s, data):
    S = [s]
    visited = [True] * 10
    for idx in data:
        visited[idx] = False
    visited[s] = True
    while S:
        curr = S.pop()
        for neigh in G[curr]:
            if visited[neigh]:
                continue
            S.append(neigh)
            visited[neigh] = True

    return visited


data = list(range(n))
min_diff = float('inf')
for i in range(1, n//2+1):
    for case in C(data, i):
        me = set(case)
        you = set(data) - me

        # if two separatable correctly
        me_space = dfs(list(me)[0], me)
        you_space = dfs(list(you)[0], you)
        if not (all(me_space) and all(you_space)):
            continue

        # get min diff of two
        me_sum = sum(population[idx] for idx in me)
        you_sum = sum(population[idx] for idx in you)

        diff = abs(me_sum - you_sum)
        min_diff = min(min_diff, diff)

print(min_diff) if min_diff != float('inf') else print(-1)

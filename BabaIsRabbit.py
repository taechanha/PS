# 3
# Rabbit is Carrot
# Baba is Cat
# Cat is Rabbit

import sys
from collections import defaultdict


def dfs(G, start):
    stack = [x for x in G[start]]
    visited = {}
    while stack:
        v = stack.pop(0)
        if v not in visited:
            for u in G[v]:
                stack.append(u)
            visited[v] = True
    return visited


def main():
    read = sys.stdin.readline
    n = int(read())
    G = defaultdict(list)
    # init Graph
    for _ in range(n):
        a, _, b = map(str, read().split())
        G[a].append(b)

    if 'Baba' not in G:
        return
    # traverse from Baba
    G = dfs(G, 'Baba')
    for case in sorted(G):
        print(case)


if __name__ == '__main__':
    main()

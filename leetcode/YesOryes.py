# 2:43 ~ 3:00

from collections import defaultdict
n, m = map(int, input().split())
G = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
s = int(input())
fans_at = set(map(int, input().split()))


def did_meet(s):
    global n, m, fans_at
    S = [s]
    visited = [False] * (n+1)
    visited[s] = True
    while S:
        curr = S.pop()
        if curr in fans_at:
            continue
        # end tour?
        if curr not in G:
            return False
        for neigh in G[curr]:
            if visited[neigh]:
                continue
            S.append(neigh)
            visited[neigh] = True
    return True


print("Yes") if did_meet(1) else print("yes")

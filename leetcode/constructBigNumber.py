import itertools
n, k = map(int, input().split())
ns = list(map(int, input().split()))
mx = 0
for ri in range(len(str(n)), 0, -1):
    for each in set(itertools.product(ns, repeat=ri)):
        curr = int("".join(map(str, each)))
        if n > curr:
            if curr > mx:
                mx = curr
print(mx)

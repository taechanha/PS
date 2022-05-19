from math import comb

n, m = map(int, input().split())
res = comb(n, m)
print(res)
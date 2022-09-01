import functools
import itertools
import sys
import math
try:
    import numpy as np
except ImportError:
    pass

stdin = sys.stdin
stderr = sys.stderr
sys.setrecursionlimit(10 ** 6)

def CP(cond, a, b):
    print(a if cond else b)
def YESNO(cond):
    CP(cond, 'YES', 'NO')
def YesNo(cond):
    CP(cond, 'Yes', 'No')
def RS():
    return sys.stdin.readline().strip()
def RI():
    return int(RS())
def RVI():
    return [int(n) for n in RS().split()]
def WVI(arr, sep=' ', **kwargs):
    print(sep.join([str(a) for a in arr]), **kwargs)

(T, ) = RVI()
for t in range(1, T+1):
    N, L = RVI()
    LT, RT = [], [] # timestamps when ant falls from left/right 
    Ps = []
    for i in range(N):
        P, D = RVI()
        if D == 0:
            LT.append(P)
        else:
            RT.append(L - P)
        Ps.append((P, i))

    Ps.sort()

    LT.sort()
    RT.sort(reverse=True)

    T = LT + RT

    DS = dict()
    for (_, i), tm in zip(Ps, T):
        if tm not in DS:
            DS[tm] = []
        DS[tm].append(i)

    ans = []
    for k in sorted(DS.keys()):
        DS[k].sort()
        for v in DS[k]:
            ans.append(v+1)

    print(f'Case #{t}: ' + ' '.join(str(n) for n in ans))

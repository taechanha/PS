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
    N, X, Y = RVI()

    S = (N + 1) * N // 2
    if S % (X + Y) != 0:
        print(f'Case #{t}: IMPOSSIBLE')
    else:
        print(f'Case #{t}: POSSIBLE')
        T = S // (X + Y) * X
        ans = []
        for i in range(N):
            n = N - i
            if T >= n:
                ans.append(n)
                T -= n
        assert T == 0
        print(len(ans))
        WVI(ans)

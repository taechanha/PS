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

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = lower.upper()
digit = '0123456789'
special = '#@*&'

def check(S1, S2):
    for c in S1:
        if c in S2:
            return True
    return False

(T, ) = RVI()
for t in range(1, T+1):
    N = RI()
    S = RS()

    for s in [lower, upper, digit, special]:
        if not check(S, s):
            S += s[0]

    if len(S) < 7:
        S += 'a' * (7 - len(S))
    print(f'Case #{t}: {S}')

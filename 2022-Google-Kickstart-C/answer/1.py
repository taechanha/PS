from sys import stdin
def input(): return stdin.readline().strip()


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


L = set('abcdefghijklmnopqrstuvwxyz')
U = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
D = set('0123456789')
S = set('#@*&')

t = read_int()
for case_num in range(1, t + 1):
    n = read_int()
    s = input()
    lower, upper, digit, char = [False] * 4
    for c in s:
        if c in L:
            lower = True
        elif c in U:
            upper = True
        elif c in D:
            digit = True
        else:
            char = True
    if not lower:
        s += 'a'
    if not upper:
        s += 'A'
    if not digit:
        s += '0'
    if not char:
        s += '#'
    if len(s) < 7:
        s += 'a' * (7 - len(s))
    print(f'Case #{case_num}: {s}')

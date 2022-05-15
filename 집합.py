import sys
input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    si = list(input().split())
    if len(si) == 2:
        si[1] = int(si[1])

    if si[0] == 'add':
        s.add(si[1])
    elif si[0] == 'remove':
        try:
            s.remove(si[1])
        except:
            pass
    elif si[0] == 'check':
        print(int(si[1] in s))
    elif si[0] == 'toggle':
        try:
            s.remove(si[1])
        except:
            s.add(si[1])
    elif si[0] == 'all':
        s = set(range(1, 21))
    else:
        s = set()
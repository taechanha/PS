from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
d = deque()

while n:
    n -= 1

    si = list(input().split())
    if len(si) == 2:
        if si[0] == 'push_back':
            d.append(si[1])
        else:
            d.appendleft(si[1])
    else:
        if si[0] == 'front':
            if d:
                print(d[0])
            else:
                print(-1)
        elif si[0] == 'back':
            if d:
                print(d[-1])
            else:
                print(-1)
        elif si[0] == 'size':
            print(len(d))
        elif si[0] == 'empty':
            if d:
                print(0)
            else:
                print(1)
        elif si[0] == 'pop_front':
            if d:
                print(d.popleft())
            else:
                print(-1)
        elif si[0] == 'pop_back':
            if d:
                print(d.pop())
            else:
                print(-1)

import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

while n:
    n -= 1
    si = list(input())[:-1]

    if len(si) % 2 != 0:
        continue
    i = 0
    while si:
        if i == len(si) - 1:
            break
        if len(si) % 2 != 0:
            break
        if si[i] == si[i+1]:
            si.pop(i)
            si.pop(i)
            i = 0
            continue
        i += 1
    else:
        cnt += 1

print(cnt)

from collections import deque

t = int(input())
while t:
    t -= 1

    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    cnt = 0
    idx2prior = deque()
    for i in range(n):
        idx2prior.append((i, prior[i]))

    # [ (0, 1), (1, 2), ... ]
    while idx2prior:
        res = idx2prior.popleft()
        if idx2prior and res[1] < max(idx2prior, key=lambda x: x[1])[1]:
            idx2prior.append(res)
        else:
            cnt += 1
            if res[0] == m:
                print(cnt)
                break
        

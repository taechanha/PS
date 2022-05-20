from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(list(range(1, n + 1)))
cnt = 0

# 1 2 3 4 5
# pop 2

for target in arr:

    # compare which is fast
    if q.index(target) > len(q) // 2:
        # op 3
        while target != q[0]:
            popped = q.pop()
            q.appendleft(popped)
            cnt += 1
    else:
        # op 2
        while target != q[0]:
            popped = q.popleft()
            q.append(popped)
            cnt += 1
    # op 1
    q.popleft()

print(cnt)

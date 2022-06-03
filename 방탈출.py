# 12:30 ~ 1:00

# 7
# 0 0 1 0 0 1 0
# 0 0 0 0 0 0 0

# 1: 0 0 0 1 1 1 0
# 2: 0 0 0 0 0 0 0

n = int(input())
lights = list(map(int, input().split()))
answer = [0] * n

next = cnt = 0
while next < n:

    if lights[next] == 1:
        # press button
        # prev = max(0, next-3)
        # if new[prev : next] == answer[prev : next]:
        cnt += 1
        lights[next: next+3] = list(map(lambda x: x ^ 1, lights[next: next+3]))
    else:
        # move by one
        next += 1

print(cnt)

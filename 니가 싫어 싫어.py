# 8:39 ~

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

data = []
for s, e in times:
    data.append((s, 1))
    data.append((e, 0))

data.sort(key=lambda x: (x[0], x[1]))

max_time_start, max_time_end, max_cnt, cnt = 0, 0, 0, 0
for time, str in data:
    if str == 1:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_time_start = time
    else:
        if cnt == max_cnt:
            max_time_end = time
        cnt -= 1

print(max_cnt)
print(max_time_start, max_time_end)

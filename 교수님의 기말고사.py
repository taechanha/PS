# 7:03

N, require_for, available_for = map(int, input().split())
schedule = [list(map(int, input().split())) for _ in range(N)]

schedule.sort(key=lambda x: x[0])

# 맨 앞 시간에 볼 수 있는 경우?
if schedule[0][0] >= require_for:
    print(0)
    exit()

# 사이에 볼 수 있는 경우?
diff = []
# 이전 시험 끝난 시간, 다음 시험 시작 시간의 차이
for i in range(N-1):
    prev_end = sum(schedule[i])
    next_start = schedule[i+1][0]
    diff.append((prev_end, next_start - prev_end))

for i, (prev_end, interval) in enumerate(diff):
    if interval >= require_for:
        print(prev_end)
        exit()

# 맨 뒤 시간에 볼 수 있는 경우?
# 요구 시간 - 마지막 시험 끝난 시간 >= 이용 가능 시간
if available_for - sum(schedule[-1]) >= require_for:
    print(sum(schedule[-1]))
    exit()
print(-1)

# 1.
# 0 1
# 4 1

# 2.
# 0 2
# 4 1

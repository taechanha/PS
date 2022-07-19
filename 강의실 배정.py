# 6:53 ~


# 3
# 1 3
# 2 4
# 3 5

n = int(input())
data = []  # s, t, diff(t-s)
for _ in range(n):
    s, t = map(int, input().split())
    data.append((s, t, t-s))

data.sort(key=lambda x: (x[0], x[2]))

s, _, _ = data[0]
prev_t = s
cnt = 0
for s, t, diff in data:
    if prev_t == s:
        prev_t = t
    else:
        cnt += 1

print(cnt)

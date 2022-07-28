# 3:27 ~ 4:03

n, L = map(int, input().split())
pools = []
min_s, max_e = float('inf'), -1
for _ in range(n):
    s, e = map(int, input().split())
    min_s, max_e = min(min_s, s), max(max_e, e)
    pools.append((s, e))

pools.sort(key=lambda x: (x[0], x[1]))

# 111222..333444555.... // 길이 3인 널빤지
# .MMMMM..MMMM.MMMM.... // 웅덩이
# 012345678901234567890 // 좌표

ans = 0
curr_pos = 0

# proceed
for s, e in pools:
    if s > curr_pos:
        curr_pos = s

    while curr_pos < e:
        curr_pos += L
        ans += 1

print(ans)

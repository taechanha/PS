# 순서 X 중복 X
n, s = map(int, input().split())
nums = list(map(int, input().split()))


def rec(i, chosen):
    global m, cnt
    if len(chosen) >= m:
        # print(chosen)
        if s == sum(chosen):
            cnt += 1
        return

    for k in range(i, n):
        chosen.append(nums[k])
        rec(k+1, chosen)
        chosen.pop()


chosen_idx = [0] * n
used = [0] * n
cnt = 0
for m in range(1, n+1):
    # 0번째부터 m개 선택
    rec(0, [])
print(cnt)

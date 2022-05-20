# 9:45 ~ 10:05

nums = list(map(int, input().split()))
cnt = 1


def get_clock_num(arr):
    min_num = float('inf')
    for _ in range(4):
        arr.append(arr.pop(0))
        min_num = min(min_num, int(''.join(map(str, arr))))
    return min_num


given = get_clock_num(nums)
clock_nums = set()
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                res = get_clock_num([a, b, c, d])
                if res >= given:
                    print(cnt)
                    exit()
                if res in clock_nums:
                    continue
                clock_nums.add(res)
                cnt += 1

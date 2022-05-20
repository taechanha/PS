

def find_zeros_idx(stones):
    ret = []
    for i in range(len(stones)):
        if stones[i] == 0:
            ret.append(i)
    return ret


def count_continuous_zeros(zeros_idx):
    # [0, 3, 4, 5, 7, 9]
    max_cnt, cnt = 1, 1
    for i in range(len(zeros_idx) - 1):
        if zeros_idx[i]+1 == zeros_idx[i+1]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1

    return max_cnt


def solution(stones, k):
    ans = 0
    # i = 0
    if len(stones) == 1:
        return stones[0]
    while sum(stones) != 0:
        zeros_idx = find_zeros_idx(stones)
        max_cnt = count_continuous_zeros(zeros_idx)
        if max_cnt >= k:
            break
        # cross
        stones = [max(0, x-1) for x in stones]
        # if i == 3:
        # print(stones)
        # exit()
        ans += 1
        # i += 1
    return ans


# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
stones = [1]
stones = [2, 1]
k = 1
res = solution(stones, k)
print(res)

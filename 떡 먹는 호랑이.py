# 9:01 ~


# D, K = 6, 41
# D, K = 7, 218
D, K = map(int, input().split())


def solution(D, K):

    for before in range(K, 0, -1):
        # [25, 41 - 25]
        diff = [before, K - before]
        cnt = 2
        flag = 0
        while True:
            cnt += 1
            curr = diff.pop(0)
            prev = diff[0]
            diff.append(curr - prev)
            if diff[0] <= diff[1]:
                flag = 1
                break
            if cnt == D-1:
                break
        if not flag:
            return diff
    return 1


res = solution(D, K)
print(res[1])
print(res[0])

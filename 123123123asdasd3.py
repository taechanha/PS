def findme(k, chosen):
    global n, dx
    if k < 0:
        return 0
    if k == 0:
        if len(chosen) != len(str(int(chosen))):
            return 0
        return 1

    acc = 0
    for i in range(n):
        acc += findme(k-dx[i], chosen+str(dx[i]))
    return acc


def solution(k):
    # global n, dx
    need = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    x = [1, 1] + [0] * 49
    for i in range(2, 8):
        x[i] = 1

    for i in range(2, k):
        for j in range(10):
            x[i + need[j]] = x[need[j]]

res = solution(11)
print(res)

# 11 -> 99

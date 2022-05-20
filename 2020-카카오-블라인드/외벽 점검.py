from itertools import permutations as Perm

# 이 문제는 내가 뼈를 갈아서라도 배워야 하는 문제다

# 1. 뭘 몰라서 손도 못댔는지 분석한다

# 2. 다음에는 어떻게 접근해야하는지 배운다.


def roll_circle(weak, n):
    # [1, 3, 4, 9, 10]
    # 초기값 제외 n - 1번에 대해서 수행하면 됨
    weak.append(weak.pop(0) + n)
    return weak


def solution(n, weak, dist):
    temp_weak = weak[:]
    dist_order = list(Perm(dist))
    glob_min = float('inf')
    # 원판 돌리기
    for _ in range(len(weak)):
        # 어떤 인원에 대해서,
        # 외벽 점검 투입 인원 카운팅
        # 어떤 한 인원 그룹마다 그 카운팅 값과 min 값 비교
        for i in range(len(temp_weak)):
            for each_order in dist_order:
                start = temp_weak[i]
                flag = 0
                # if temp_weak == [10, 13, 17, 18] and each_order[0] == 4 and each_order[1] == 2:
                # 외벽 점검 [1, 3, 4, 9, 10] - [3, 5, 7]
                for j in range(len(each_order)):
                    start += each_order[j]
                    if start >= temp_weak[-1]:
                        glob_min = min(glob_min, j + 1)
                        flag = 1
                        break
                    for k in range(len(temp_weak)):
                        if temp_weak[k] >= start:
                            start = temp_weak[k]
                            break
                
        temp_weak = roll_circle(temp_weak, n)

    return glob_min


n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
weak = [10, 13, 17, 18]
dist = [4, 2, 1, 3]

# n = 12
# weak = [1, 3, 4, 9, 10]
# dist = [3, 5, 7]
res = solution(n, weak, dist)

print(res)

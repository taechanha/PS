from itertools import product


def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


print(solution([1, 1, 1, 1, 1], 3))

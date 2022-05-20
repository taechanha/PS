from collections import deque
from sys import stdin
input = stdin.readline


def solution():
    n, d, k, c = map(int, input().split())

    line = [int(input()) for _ in range(n)]
    line += line[:k-1]

    max_kinds = 0
    unique_sushi = set(line[:k-1])
    prev = deque(line[:k-1])

    for i in range(k, n+k-1):
        flag = 0

        prev.append(line[i])
        unique_sushi.add(line[i])

        if c not in unique_sushi:
            flag = 1
        max_kinds = max(max_kinds, len(unique_sushi)+flag)

        # if len(unique_sushi)+flag == 4:
        #     print(unique_sushi, prev, i)

        popped = prev.popleft()
        unique_sushi.remove(popped)

    return max_kinds


res = solution()
print(res)

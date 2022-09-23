# 2
# ababa
# aba
# abracadabra
# ab

from collections import defaultdict


def solution():
    T = int(input())
    for i in range(1, T+1):
        cache = defaultdict(int)
        book = input()
        target = input()
        n, m = len(book), len(target)

        for j in range(n):
            for k in range(j+1, n):
                word = book[j:k]
                cache[word] += 1

        answer = 0
        if target in cache:
            answer = cache[target]

        print(f"#{i} {answer}")


solution()

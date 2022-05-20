# test = "17 11 16 1 19 18 13 12 8 13"
# # test = "3 3 5 14 5 11 17 18 1 5 13 14 3 14 18 6 2 7 13 13"
# # test = "1 4 4 12 3 17 18 4"
# test = test.split()
# test = [int(x) for x in test]

import sys

read = sys.stdin.readline
T = int(read())

for i in range(1, T + 1):
    k = int(read())
    test_case = list(map(int, read().split()))
    yuna_points, opposite_points = 0, 0
    evens = [x for x in test_case if x % 2 == 0]
    odds = [x for x in test_case if x % 2 != 0]
    while len(evens) > 1:
        max_evens = evens.pop(evens.index(max(evens)))
        min_evens = evens.pop(evens.index(min(evens)))
        yuna_points += max(max_evens, min_evens)

    while len(odds) > 1:
        max_odds = odds.pop(odds.index(max(odds)))
        min_odds = odds.pop(odds.index(min(odds)))
        yuna_points += max(max_odds, min_odds)

    if evens or odds:
        yuna_points += min(evens.pop(), odds.pop())

    print('#{} {}'.format(i, yuna_points))

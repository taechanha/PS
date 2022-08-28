# 0 1
# 1 3
# 2 5
# 3 4
# 4 0
# 5 2

import sys


def set_game():
    read = sys.stdin.readline
    N, K = map(int, read().split())
    a = []
    for _ in range(N):
        a.append(int(read()))

    return a, N, K


def main():
    a, N, K = set_game()
    start_game(a, N, K)


def start_game(a, N, K):
    turn = 0
    i = 0
    while turn < N:
        if a[i] == K:
            print(turn + 1)
            return

        # "i+1" !
        i = a[i]
        turn += 1

    print(-1)


if __name__ == '__main__':
    main()

import sys
read = sys.stdin.readline


def to_the_moon(row, y, prev_dir, chosen):
    if row >= n:
        answer.append(chosen)
        return
    else:
        for i in range(m):
            dy = y + ydir[i]
            if prev_dir != i and is_valid_pos(dy):
                # print(row, col, n, m)
                chosen += board[row][dy]
                to_the_moon(row + 1, dy, prev_dir, chosen)


def is_valid_pos(col):
    if col < 0 or col >= m:
        return False
    return True


def main():
    global ydir, n, m, board, answer
    n, m = map(int, read().split())
    ydir = [-1, 0, 1]
    board = []
    answer = []
    for _ in range(n):
        board.append(list(map(int, read().split())))

    for i in range(m):
        to_the_moon(0, i, -1, 0)

    # print(answer)
    print(min(answer))


if __name__ == '__main__':
    main()

def count(s):
    return s.count('*')


def count_by_row(board, start_i, start_j, n):
    cnt = 0
    for i in range(start_i, n):
        if board[i][start_j] == '*':
            cnt += 1
    return cnt


def main():
    n = int(input())
    board = []
    for i in range(n):
        board.append(input())

    for i in range(len(board)):
        for j in range(len(board[0])):
            # 1. find head
            if board[i][j] == '*':
                # 2. heart is at (x, y+1)
                heart = [i+2, j+1]
                # 3. left hand length
                left_hand_len = count(board[i+1][:j])
                # 4. right hand length
                right_hand_len = count(board[i+1][j+1:])
                # 5. waist length
                waist_len = count_by_row(board, i, j, n) - 2
                # 6. right leg length
                left_leg_len = count_by_row(board, i, j-1, n) - 1
                # 7. left leg length
                right_leg_len = count_by_row(board, i, j+1, n) - 1

                print(*heart)
                print(left_hand_len, right_hand_len,
                      waist_len, left_leg_len, right_leg_len)
                return


if __name__ == "__main__":
    main()

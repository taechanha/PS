n, m = map(int, input().split())

raw_board = [input() for _ in range(n)]
min_cnt = float('inf')

for k in range(n - 8 + 1):
    for l in range(m - 8 + 1):
        # raw_board[k:k+8][l:l+8]
        board = [row[l:l+8] for row in raw_board[k:k+8]]
        
        if board[0][0] == 'W':
            flag = 'W'
            flag2 = 'B'
        else:
            flag = 'B'
            flag2 = 'W'

        cur_cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if board[i][j] != flag:
                            cur_cnt += 1
                    else:
                        if board[i][j] != flag2:
                            cur_cnt += 1
                else:
                    if j % 2 == 0:
                        if board[i][j] != flag2:
                            cur_cnt += 1
                    else:
                        if board[i][j] != flag:
                            cur_cnt += 1

        if min_cnt > cur_cnt:
            min_cnt = cur_cnt

print(min_cnt)
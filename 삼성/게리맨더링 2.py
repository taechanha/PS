# (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

board = [[0] * n for _ in range(n)]
min_diff = float('inf')

for d1 in range(1, n):
    for d2 in range(1, n):
        for r in range(n):
            if not (0 <= r < r+d1+d2 <= n-1):
                continue
            for c in range(n):
                if not (0 <= c-d1 < c < c+d2 <= n-1):
                    continue
                board = [[0] * n for _ in range(n)]
                # (x, y), (x+1, y-1), ..., (x+d1, y-d1)
                for delta in range(d1+1):
                    board[r+delta][c-delta] = 5
                # (x, y), (x+1, y+1), ..., (x+d2, y+d2)
                for delta in range(d2+1):
                    board[r+delta][c+delta] = 5
                # (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
                for delta in range(d2+1):
                    board[r+d1+delta][c-d1+delta] = 5
                # (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
                for delta in range(d1+1):
                    board[r+d2+delta][c+d2-delta] = 5

                for row in range(n):
                    saved = False
                    for col in range(n):
                        if board[row][col] == 5:
                            if saved:
                                for cur_c in range(saved, col+1):
                                    board[row][cur_c] = 5
                                break
                            saved = col

                # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
                for cur_r in range(r+d1):
                    for cur_c in range(c+1):
                        if board[cur_r][cur_c] != 0:
                            continue
                        board[cur_r][cur_c] = 1
                # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
                for cur_r in range(r+d2+1):
                    for cur_c in range(c, n):
                        if board[cur_r][cur_c] != 0:
                            continue
                        board[cur_r][cur_c] = 2
                # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
                for cur_r in range(r+d1, n):
                    for cur_c in range(c-d1+d2):
                        if board[cur_r][cur_c] != 0:
                            continue
                        board[cur_r][cur_c] = 3
                # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
                for cur_r in range(r+d2, n):
                    for cur_c in range(c-d1+d2, n):
                        if board[cur_r][cur_c] != 0:
                            continue
                        board[cur_r][cur_c] = 4

                # if (r, c, d1, d2) == (1, 3, 2, 2):
                #     print(r, c, d1, d2)
                #     for row in board:
                #         print(row)
                #     print()

                # 선거구 인구
                sums = [0, 0, 0, 0, 0]
                for i in range(n):
                    for j in range(n):
                        sums[board[i][j]-1] += city[i][j]

                # 각 선거구 인원 차이의 최솟값
                min_sum = min(sums)
                max_sum = max(sums)
                min_diff = min(min_diff, max_sum-min_sum)

print(min_diff)

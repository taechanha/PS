# 2:46 ~ 3:06

# 1 ~ 100크기의 모든 십자가 모양을 각 배열을 2중 포문으로 순회하면서
# 1이 되면 2가 되는지 --- 100까지

# so, TC would be 100x100x400 = 4,000,000

n, m = map(int, input().split())
size = min(n, m) + 1
board = [input() for _ in range(n)]
# 가능한 십자가 모양 만들기
print(board, len(board), len(board[0]), n, m)


def check(r, c, size):
    # up, down, left, right
    cnt = 0
    for i in range(1, size+1):
        if not (0 <= r+i < n and board[r+i][c] == '*'):
            break
        if not (0 <= r-i < n and board[r-i][c] == '*'):
            break
        if not (0 <= c+i < m and board[r][c+i] == '*'):
            break
        if not (0 <= c-i < m and board[r][c-i] == '*'):
            break
        cnt += 1
    return cnt


# 2중 포문을 돌며 각 십자가 체크
cnt = 0
for r in range(n):
    for c in range(m):
        cnt += check(r, c, size)

print(cnt)
# print(-1) if cnt == 0 else print(cnt)

# import sys
# read = sys.stdin.readline

# def helper(board, i, j, chosen, s):
#     if len(chosen) == len(s):
#         if chosen == s:
#              return 1
#     else:
#         chosen.append(board[i+1][j])
#         helper(board, i + 1, j, chosen, s)

# def number_of_cases(board, s):
#     cnt = 0
#     for each in s:
#         helper(board, 0, 0, "", each)
#     return cnt

# def main():
#     n, m, k = map(int, read().split())
#     board = []

#     for _ in range(n):
#         board.append(read())

#     for _ in range(k):
#         s = read()
#         print(number_of_cases(board, s))


# if __name__ == '__main__':
#     main()

n, m, k = map(int, input().split())
str = [input() for i in range(n)]
mp = {}


def solve():
    s = input()
    if s in mp:
        print(mp[s])
    else:
        print(0)


def dfs(x, y, pos, sum):
    if pos >= 5:
        return
    mp[sum] = mp.get(sum, 0) + 1
    for i in range(8):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0:
            tx = n - 1
        if tx >= n:
            tx = 0
        if ty < 0:
            ty = m - 1
        if ty >= m:
            ty = 0
        dfs(tx, ty, pos + 1, sum + str[tx][ty])


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

for i in range(n):
    for j in range(m):
        dfs(i, j, 0, str[i][j])

while k:
    solve()
    k -= 1

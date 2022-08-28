
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
# # matrix = [["0", "1"], ["1", "0"]]
# # matrix = [["0"]]


# def dfs(r, c):
#     s = [(r, c)]
#     visited[r][c] = True
#     cnt = 1
#     while s:
#         cr, cc = s.pop()

#         for i in range(len(dr)):
#             nr = cr + dr[i]
#             nc = cc + dc[i]

#             if not (0 <= nr < n and 0 <= nc < m):
#                 continue
#             if visited[nr][nc]:
#                 continue
#             if matrix[nr][nc] == '0':
#                 continue

#             s.append((nr, nc))
#             visited[nr][nc] = True
#             cnt += 1

#     return cnt


# # right, down, up, left
# dr = [0, 1, -1, 0]
# dc = [1, 0, 0, -1]
# n = len(matrix)
# m = len(matrix[0])
# visited = [[False]*m for _ in range(n)]  # [n][m]
# max_cnt = 0
# # for i in range(n):
# #     for j in range(m):
# #         if visited[i][j]:
# #             continue
# #         if matrix[i][j] == '0':
# #             continue
# #         curr_cnt = dfs(i, j)
# #         if curr_cnt > max_cnt:
# #             max_cnt = curr_cnt
# print(max_cnt)
# ------------------------------------------------------


# sub-problem:
# a(i, j) = area of matrix(:i, :j),
# Ex 1. a(0, 0) = area of matrix(0, 0) = matrix[0][0]
# Ex 2. a(1, 1) = area of matrix(:1, :1) = matrix[0][0] + matrix[0][1] + matrix[1][0]
# relate:
# a(i, j) = min(a(i, j), a(i + 1, j), a(i, j + 1)) + 1, if matrix[i][j] = 1

rows = len(matrix)
cols = len(matrix[0])
dp = [[0]*(cols + 1) for _ in range(rows + 1)]  # dp[rows][cols]
max_cnt = 0
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == '0':
            continue
        dp[r+1][c+1] = min(dp[r][c], dp[r][c+1], dp[r+1][c]) + 1
        max_cnt = max(max_cnt, dp[r+1][c+1])

print(pow(max_cnt, 2))

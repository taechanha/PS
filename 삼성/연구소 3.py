# # 바이러스가 놓일 수 있는 모든 위치 조합에 각 조합의 여러 정점을 시작점으로 하는 DFS
# # 이후 결과 배열을 순회하며 벽이나 바이러스가 아닌 칸 중 빈 칸이 있는 지 확인 -> -1 출력 혹은 최댓값(=시간) 출력

# # (numOf2)Cm
# from itertools import combinations as C

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# dr = [1, -1, 0, 0, ]
# dc = [0, 0, 1, -1]


# def dfs(coords):
#     global board
#     S, dist = [], dict()
#     for r, c in coords:
#         S.append((r, c))
#         dist[(r, c)] = 0
#         board[r][c] = 

#     while S:
#         r, c = S.pop()

#         for i in range(n):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if not (0 <= nr < n and 0 <= nc < n):
#                 continue
#             if (nr, nc) in dist:
#                 continue
#             if board[nr][nc] != 0:
#                 continue
#             S.append((nr, nc))
#             dist[(nr, nc)] = dist[(r, c)] + 1


# viruses = []
# walls = []
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 2:
#             viruses.append((i, j))
#         elif board[i][j] == 1:
#             walls.append((i, j))

# combs = list(C(viruses, m))

# for comb in combs:
#     temp = [row[:] for row in board]
#     for r, c in comb:
#         board[r][c] = '*'
#     dfs(comb)

#     board = [row[:] for row in temp]
    

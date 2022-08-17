# rerere
# 3:08 ~ 3:38

# 7 3
# 1110110
# 1011001

import sys
sys.setrecursionlimit(10**6)


n, k = map(int, input().split())
left = list(input())
right = list(input())


def dfs(i, left_side, d):
    # base case
    if i < 0 or i < d:
        return 0
    if i >= n:
        memo[(i, left_side)] = 1
        return 1
    if left_side:
        if left[i] == '0':
            return 0
    else:
        if right[i] == '0':
            return 0
    if (i, left_side) in memo:
        return memo[(i, left_side)]
    if left_side:
        memo[(i, left_side)] = dfs(i+k, 0, d+1)  # move to right
    else:
        memo[(i, left_side)] = dfs(i+k, 1, d+1)  # move to left
    # move forward
    case1, case2 = 0, 0
    case1 = dfs(i+1, left_side, d+1)
    # move backward
    case2 = dfs(i-1, left_side, d+1)
    # move the opposite side
    memo[(i, left_side)] = case1 | case2
    return memo[(i, left_side)]


memo = {}
ret = dfs(0, 1, 0)
print(1) if ret else print(0)


# answer code

# import sys
# from collections import deque
# sys.stdin = open('백준15558. 점프 게임.txt', 'r')
# N, k = map(int, input().split())
# lines = [sys.stdin.readline().rstrip() for _ in range(2)]
# queue = deque([(0, 0)])
# visited = [[0]*N for _ in range(2)]
# time = -1
# flag = False
# while queue:
#     for _ in range(len(queue)):
#         d, idx = queue.popleft()
#         # 게임 클리어
#         if idx+1 >= N or idx+k >= N: 
#             flag = True
#             break
#         # 한 칸 앞으로 이동
#         if int(lines[d][idx+1]) and not visited[d][idx+1]: 
#             queue.append((d, idx+1))
#             visited[d][idx+1] = 1
#         # 한 칸 뒤로 이동
#         if idx-1 > time+1 and int(lines[d][idx-1]) and not visited[d][idx-1]: 
#             queue.append((d, idx-1))
#             visited[d][idx-1] = 1
#         # 반대편 줄 & k칸 앞으로 이동
#         if int(lines[(d+1)%2][idx+k]) and not visited[0][idx+k]: 
#             queue.append(((d+1)%2, idx+k))
#             visited[(d+1)%2][idx+k] = 1
#     time += 1
# print(1) if flag else print(0)
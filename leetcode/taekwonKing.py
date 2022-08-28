# # def min_kicks(s, t):
# #     store = []
# #     i = 0
# #     while s != t:
# #         cnt = i
# #         temp_s = s
# #         temp_t = t
# #         while temp_s * 2 <= temp_t + 3:
# #             temp_s *= 2
# #             temp_t += 3
# #             cnt += 1

# #         if temp_s == temp_t:
# #             store.append(cnt)
# #         else:
# #             store.append(cnt + temp_t - temp_s)

# #         s += 1
# #         i += 1

# #     return min(store)


# # def main():
# #     # n = int(input())
# #     answer = []
# #     test = [[10, 37]]

# #     for s, t in test:
# #         # s, t = map(int, input().split())
# #         answer.append(min_kicks(s, t))

# #     for min_kick in answer:
# #         print(min_kick)


# # if __name__ == "__main__":
# #     main()

# #
# # ----------------------------------------------------------------------------------
# #


# def find(start, target, count, chosen):
#     if count != 0 and chosen != [] and min(chosen) < count:
#         return
#     print(start, target, count, chosen)
#     if start == target:
#         chosen.append(count)
#     else:
#         while start != target:
#             if start * 2 <= target + 3:
#                 find(start * 2, target + 3, count + 1, chosen)
#             else:
#                 find(start + 1, target, count + 1, chosen)
#                 break

#             start += 1
#             count += 1


# # def bfs(graph, start, visited):
# #     queue = deque([start])
# #     visited[start] = True
# #     while queue:
# #         v = queue.popleft()
# #         for u in graph[v]:
# #             if not visited[u]:
# #                 queue.append(current * 2, target + 3, count + 1)
# #                 queue.append(current, target, count + 1)
# #                 visited[u] = True


# def bfs(s, t):
#     q = deque([(s, t, 0)])
#     visited = {}
#     while q:
#         print(q)
#         v, t, cnt = q.popleft()

#         if v == t:
#             return cnt

#         if v <= t and v not in visited:
#             if v * 2 <= t + 3:
#                 q.append((v * 2, t + 3, cnt + 1))
#             q.append((v + 1, t, cnt + 1))
#             visited[v] = True


# def main():
#     # n = int(input())
#     # test = [[10, 20], [2, 7], [15, 62], [10, 37], [11, 50], [34, 59]]
#     test = [[10, 37]]
#     for s, t in test:
#         # s, t = map(int, input().split())
#         # find(s, t, 0, [])
#         print(bfs(s, t))


# if __name__ == "__main__":
#     main()

from collections import deque


def bfs(s, t):
    q = deque([(s, t, 0)])
    visited = {}
    while q:
        v, t, cnt = q.popleft()
        if v <= t and v not in visited:
            q.append((v * 2, t + 3, cnt + 1))
            q.append((v + 1, t, cnt + 1))
            visited[v] = True
            if v == t:
                return cnt


n = int(input())
answer = []
for _ in range(n):
    s, t = map(int, input().split())
    answer.append(bfs(s, t))
for each in answer:
    print(each)


def bfs(S, T):
    q = deque()
    q.append((S, T, 0))
    check = [-1]*(200)
    while q:
        node, t, c = q.popleft()
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c+1))
            q.append((node+1, t, c+1))
            check[node] = 1
            if node == t:
                return c


C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))

# from collections import deque
# import heapq


# def bfs(s, t):
#     # q = deque()
#     heap = []
#     heapq.heappush(heap, (s, t, 0))
#     # q.append((s, t, 0))
#     visited = {}
#     while heap:
#         s, t, c = heapq.heappop(heap)
#         # s, t, c = q.popleft()
#         if s == t:
#             return c
#         if s not in visited:
#             if s > t and s % 2 == 0:
#                 heapq.heappush(heap, (s // 2, t, c + 1))
#                 # q.append((s // 2, t, c + 1))
#             heapq.heappush(heap, (s + 1, t, c + 1))
#             # q.append((s + 1, t, c + 1))
#             visited[s] = True


# a, b = map(int, input().split())

# print(bfs(a, b))

import sys
sys.setrecursionlimit(10**6)


def dfs(s, t, c):
    if s == t:
        return c
    else:
        if s > t:
            if s % 2 == 0:
                return dfs(s // 2, t, c + 1)
            else:
                return dfs(s + 1, t, c + 1)
        else:
            return t - s + c


# def dfs(s, t, c):
#     # s = 27, t = 103
#     if s < 1:
#         return
#     elif s == t:
#         return c
#     else:
#         if s < t and s % 2 == 0:
#             return dfs(s * 2, t, c + 1)

#         return dfs(s - 1, t, c + 1)


def main():
    a, b = map(int, sys.stdin.readline().split())
    print(dfs(a, b, 0))


if __name__ == "__main__":
    main()
# a, b = map(int, input().split())
# cnt = 0

# if a == b:
#     print(0)
# elif a < b:
#     print(b - a)
# while a > b:
#     if a % 2 == 0:
#         a //= 2
#     else:
#         a += 1
#     cnt += 1

# print(cnt + b - a)

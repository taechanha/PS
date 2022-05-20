import heapq


def solution(n, m, a, x, y):
    # Type your solution here
    # BFS
    # Time: O(n*m)
    # Space: O(n*m)
    # n: number of rows
    # m: number of columns
    # a: matrix of frog food
    # k: number of jumps
    # x: frog's location
    # y: frog's house location
    # return: minimum number of jumps
    if n == 0 or m == 0:
        return -1
    if x == y:
        return 0
    queue = []
    visited = set()
    heapq.heappush(queue, (0, x))
    visited.add(x)
    while queue:
        curr_dist, curr_loc = heapq.heappop(queue)
        if curr_loc == y:
            return curr_dist
        for next_loc in get_next_locations(curr_loc, n, m, a):
            if next_loc not in visited:
                heapq.heappush(queue, (curr_dist + 1, next_loc))
                visited.add(next_loc)
    return -1


def get_next_locations(curr_loc, n, m, a):
    next_locations = []
    x, y = curr_loc
    if x - a[x-1][y-1] >= 1:
        next_locations.append((x - a[x-1][y-1], y))
    if x + a[x-1][y-1] <= n:
        next_locations.append((x + a[x-1][y-1], y))
    if y - a[x-1][y-1] >= 1:
        next_locations.append((x, y - a[x-1][y-1]))
    if y + a[x-1][y-1] <= m:
        next_locations.append((x, y + a[x-1][y-1]))
    return next_locations


N, M = map(int, input().split())
r_f, c_f, r_h, c_h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]

res = solution(N, M, a, (r_f, c_f), (r_h, c_h))
print(res)

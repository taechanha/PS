import sys
from collections import deque
input = sys.stdin.readline


def distance(from_x, from_y, to_x, to_y):
    return abs(from_x - to_x) + abs(from_y - to_y)


def bfs(target, s):
    q = deque()
    q.append([s[0], s[1]])
    # if n: 2, visited will be [conv1, conv2, target]
    visited = [False for i in range(n+1)]
    # meaning "source" doesn't have to be in there
    while q:
        curr_x, curr_y = q.popleft()
        if distance(curr_x, curr_y, target[0], target[1]) <= 1000:
            print("happy")
            return
        for i in range(n):  # loop through conv; 0-th conv, 1-th conv, ..., n-1-th conv
            if not visited[i]:
                curr_conv_x, curr_conv_y = conv[i]
                if distance(curr_x, curr_y, curr_conv_x, curr_conv_y) <= 1000:
                    q.append([curr_conv_x, curr_conv_y])
                    visited[i] = True
    print("sad")


t = int(input())
while t:
    t -= 1
    n = int(input())
    source = list(map(int, input().split()))  # Ex. [0, 0]
    conv = [list(map(int, input().split()))
            for _ in range(n)]  # Ex. [[1000, 0], [1000, 1000]]
    target = list(map(int, input().split()))  # Ex. [2000, 1000]
    bfs(target, source)

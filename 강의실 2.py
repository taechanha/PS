# 3:50 ~

import heapq

n = int(input())
classroom = {}
time_table = []

for _ in range(n):
    idx, start, end = map(int, input().split())
    time_table.append((idx, start, end))

time_table.sort(key=lambda x: x[1])

for time in time_table:
    idx, start, end = time
    for k, v in classroom.items():
        

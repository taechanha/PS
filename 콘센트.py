# 3:05 ~ 3:27

# 분배 문제
# 8 4 4 1 1
# M 크기의 bucket
import heapq

n, m = map(int, input().split())
bucket = [0] * m
device = sorted(map(int, input().split()), reverse=True)

for charge_time in device:
    accum_time = heapq.heappop(bucket)
    accum_time += charge_time
    heapq.heappush(bucket, accum_time)

print(max(bucket))

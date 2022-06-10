import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

# 총 감독관 넣기
for i in range(n):
    a[i] -= b

# 부 감독관 넣기
for i in range(n):
    if a[i] <= 0:
        continue
    cnt += math.ceil(a[i] / c)


print(cnt + n)

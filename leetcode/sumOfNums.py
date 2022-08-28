n, m = map(int, input().split())
cnt = 0
arr = list(map(int, input().split()))
p1, p2 = 0, 1

while p2 < n + 1:
    summed = sum(arr[p1:p2])
    if summed == m:
        cnt += 1
        p1 += 1
    elif summed > m:
        p1 += 1
    else:
        p2 += 1


print(cnt)


# for i in range(n):
#     tmp.append(arr[i])

#     if sum(tmp) > m:
#         tmp.pop(0)

#     if sum(tmp) == m:
#         cnt += 1
#         tmp.pop(0)

# while i < n:

#     tmp.append(arr[i])
#     accum = sum(tmp)

#     if accum > m:
#         accum.pop(0)

#     if accum == m:
#         cnt += 1
#         accum.pop(0)


# 4 2
# 1 1 1 1

# 10 5
# 1 2 3 4 2 5 3 1 1 2

# # two-pointers

# 10 15
# 5 1 3 5 10 7 4 9 2 8

n, s = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
sum = 0
ans = 1000000000

while 1:
    if sum >= s:
        ans = min(ans, end - start)
        sum -= arr[start]
        start += 1
    else:
        sum += arr[end]
        end += 1

    if start >= end and end >= n:
        break
print(ans)

# if sum < s:
#         sum += arr[end]
#         end += 1
#     elif sum == s:
#         sum -= arr[start]
#         start += 1
#         ans = min(ans, end - start + 1)
#     else:
#         sum -= arr[start]
#         start += 1

# 누적합 문제

n = int(input())
nums = sorted(list(map(int, input().split())))
prefix_sum = [0] * len(nums)
prefix_sum[0] = nums[0]

for i in range(1, len(nums)):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

print(sum(prefix_sum))
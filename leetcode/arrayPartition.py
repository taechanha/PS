# n개의 페어를 이용한 min(a, b)의 합으로
# 만들 수 있는 가장 큰 수를 출력
def array_partition(nums):
    max = 0
    nums.sort()
    return min(nums[0], nums[1]) + min(nums[-1], nums[-2])


test_cases = [
    [1, 4, 3, 2]
]

for case in test_cases:
    print(array_partition(case))

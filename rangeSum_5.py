n, m = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
print(nums)


def partial_sum(nums):
    psum = [[0] * len(nums[0])] * len(nums)
    for i in range(len(nums)):
        psum[i][0] = nums[i][0]
        for j in range(1, len(nums[0])):
            psum[i][j] = psum[i][j-1] + nums[i][j]
    return psum


print(partial_sum(nums))

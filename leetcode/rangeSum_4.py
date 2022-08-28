n, m = map(int, input().split())
nums = list(map(int, input().split()))


def partial_sum(nums):
    psum = [0] * len(nums)
    psum[0] = nums[0]
    for i in range(1, len(nums)):
        psum[i] = psum[i-1] + nums[i]
    return psum


psum = partial_sum(nums)

for _ in range(m):
    j, k = map(int, input().split())

    if j < 1:
        print(psum[k])
    else:
        print(psum[k] - psum[j-1])

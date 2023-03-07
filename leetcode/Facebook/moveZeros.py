# // 6.32 -

# // Input: nums = [0,1,0,3,12]
# // Output: [1,3,12,0,0]

def moveZeros(nums):
    inds = []
    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            inds.append(i)
    cnt = len(inds)
    for i in inds[::-1]:
        nums.pop(i)

    nums += [0] * cnt
    return nums


nums = [0, 1, 0, 3, 12]
ans = moveZeros(nums)

print(ans)

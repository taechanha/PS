# def bsearch(nums, i, j, t):
#     mid = i + (j - i) // 2
#     if nums[mid] == t:
#         return mid
#     elif i == j:
#         return -1
#     elif nums[mid] > t:
#         return bsearch(nums, i, mid, t)
#     elif nums[mid] < t:
#         return bsearch(nums, mid + 1, j, t)

# nums = [-1, 0, 3, 5, 9, 12]
# print(bsearch(nums, 0, len(nums) - 1, 2))

nums = [1,3,5,6]
target = 5
left, right = 0, len(nums) - 1
while left < right:
    mid = left + (right - left) // 2
    if nums[mid] > target:
        right = mid
    elif nums[mid] < target:
        left = mid + 1
print(left)
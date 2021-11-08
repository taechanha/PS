# def product_except_self(nums):
#     p = 1
#     out = []
#     for i in range(len(nums)):
#         out.append(p)
#         p *= nums[i]
#         print(out)

#     p = 1
#     for i in range(len(nums) - 1, 0 - 1, -1):
#         out[i] *=  p
#         p *= nums[i]
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    if not nums:
        return False

    arr = [1] * len(nums)
    pi = pj = 1

    for i in range(len(nums)):
        j = -1-i

        print(i, j, arr, pi, pj)

        arr[i] *= pi
        arr[j] *= pj
        pi *= nums[i]
        pj *= nums[j]

        print(i, j, arr, pi, pj, '\n')
    return arr


test_cases = [
    [1, 2, 3, 4]
]

for case in test_cases:
    print(productExceptSelf(case))

def sum_of_three(nums):
    answer = []
    nums.sort()
    left, right = 0, len(nums) - 1
    prev = -1
    while left < right:
        if sum > 0:
            prev = left
            left += 1
        elif sum < 0:
            prev = right
            right -= 1
        else:
            left += 1
            right -= 1
            answer.append([nums[prev], nums[left], nums[right]])

    return answer


test_cases = [
    [-1, 0, 1, 2, -1, 4]
]

for case in test_cases:
    print(sum_of_three(case))

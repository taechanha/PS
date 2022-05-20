def twoSum(numbers, target):
    for i in range(len(numbers)):
        l, r = i+1, len(numbers)
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r-l)//2
            if numbers[mid] == tmp:
                return [i+1, mid+1]
            elif numbers[mid] < tmp:
                l = mid + 1
            else:
                r = mid - 1


print(twoSum([1, 2, 3, 4, 5], 6))

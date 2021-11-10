def maxSubarrayValue(arr):
    max_value = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            value = 0
            for k in range(i, j+1):
                value += arr[k]
            if value > max_value:
                max_value = value
    return max_value


print(maxSubarrayValue([2, -1, -4, 5]))

# Driver Code
if __name__ == '__main__':

    arr = [2, -1, -4, 5]

    # Size of array
    N = len(arr)

    # Function Call
    maxSubarrayValue(arr)

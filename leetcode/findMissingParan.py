def solution(numbers, k):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    swaps = 0
    for i in range(len(numbers)):
        while numbers[i] - numbers[i-1] > k:
            temp = numbers[i]
            numbers[i] = numbers[i-1]
            numbers[i-1] = temp
            swaps += 1
    return swaps


print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))

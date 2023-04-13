T = int(input())
_ = input()
A = list(map(int, input().split()))
_ = input()
B = list(map(int, input().split()))


# initialize a counter for the number of subarray pairs
num_pairs = 0

# loop over all possible subarrays of A
for i in range(1, len(A)+1):
    for j in range(i, len(A)+1):
        # compute the sum of the subarray A[i:j]
        sum_A = sum(A[i-1:j])
        # loop over all possible subarrays of B
        for k in range(1, len(B)+1):
            for l in range(k, len(B)+1):
                # compute the sum of the subarray B[k:l]
                sum_B = sum(B[k-1:l])
                # check if the sum of the two subarrays is equal to T
                if sum_A + sum_B == T:
                    # increment the counter if the condition is met
                    num_pairs += 1

# print the number of subarray pairs
print(num_pairs)

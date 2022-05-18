# n = int(input())
# nums = [int(input()) for _ in range(n)]
# ans = []
# stack = []
# for i in range(1, curr_max_val(nums)+1):
#     stack.append((i, 1))

# # + + + + - - + + - + + - - - - -
# curr_max_val = 0
# for query in nums:

#     while stack[curr_max_val][0] < query:

#         if stack[curr_max_val][1] != 0:
#             ans.append('+')
#         curr_max_val += 1

#     if stack[curr_max_val][0] == query:
#         stack[curr_max_val][1] = 0
#         curr_max_val -= 1
#         ans.append('-')

#     while stack[curr_max_val][1] != 0:
#         curr_max_val -= 1


# print(ans)


n = int(input())
arr = [int(input()) for _ in range(n)]
curr_max_val = 0
left = []
right = []
answer = []

while curr_max_val < arr[0]:
    left.append(curr_max_val+1)
    answer.append('+')
    curr_max_val += 1

top = len(left) - 1
right = list(range(arr[0]+1, max(arr)+1))

for each in arr:
    if each == left[top]:
        left.pop()
        answer.append('-')
        top -= 1
    # [1 2] [5 6 7 8]
    elif left[top] < each:
        for _ in range(each - curr_max_val):
            left.append(right.pop(0))
            answer.append('+')
        left.pop()
        answer.append('-')
        top += each - curr_max_val - 1
        curr_max_val = each
        # [1 2 5 6] [7 8]
        # top: 3 cmv: 6


# print(curr_max_val, left, right)
# [1 2 3 4 5 6 7 8]
# [4 3 6 8 7 5 2 1]
print(answer)

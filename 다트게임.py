# 012345678910
# SDT
# *#

# Ex.
# 1D# 2S* 3S
# 1^2 * (-1) * 2 + 2^1 * 2 + 3^1

# 딱 3세트만 주어진다.

# 10D 2S# 10S
def seperate_nums_ops(dartResult):
    nums = []
    ops = []
    acc_num = ""
    acc_str = ""
    for each in dartResult:

        if each.isdigit():
            if acc_str != "":
                ops.append(acc_str)
                acc_str = ""
            acc_num += each
        else:
            if acc_num != "":
                nums.append(int(acc_num))
                acc_num = ""
            acc_str += each

    # append remaining ops
    ops.append(acc_str)
    return nums, ops


def apply_ops(num, op):

    if op[0] == 'S':
        res = num
    elif op[0] == 'D':
        res = pow(num, 2)
    elif op[0] == 'T':
        res = pow(num, 3)

    flag = 0
    if len(op) == 2:
        if op[1] == '#':
            res = -res
        elif op[1] == '*':
            res *= 2
            flag = 1

    if flag == 1:
        return res, 1
    return res, 0


def solution(dartResult):
    nums, ops = seperate_nums_ops(dartResult)
    print(nums, ops)
    ans = []
    for i, (num, op) in enumerate(zip(nums, ops)):
        res, flag = apply_ops(num, op)
        # 이전 iteration에서의 결과 값
        ans.append(res)
        if flag and i != 0:
            ans[i-1] *= 2
    # answer
    return sum(ans)


dartResult = "1D2S3T*"
res = solution(dartResult)
print(res)

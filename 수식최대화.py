from itertools import permutations as P
from itertools import combinations as C
from collections import deque

# * + -
# * - +
# + * -
# + - *
# - * +
# - + *


def solution(exp: str):
    operand, operator = seperate_ops(exp)
    sorted_operator = sort_out_ops(operator)
    ans = []

    # Ex. [[* + -], [* - +], ...]
    for each_op_set in P(sorted_operator):
        temp_operand = operand[:]
        print(temp_operand, each_op_set, operator)
        # 우선순위 Ex. * + -
        for imp_op in each_op_set:
            # 실제 operators; - + *
            for i, each_op in enumerate(operator):
                print(temp_operand)
                if each_op == imp_op:
                    #operand1 = temp_operand.pop(i)
                    #operand2 = temp_operand.pop(i+1)
                    res = apply_ops(
                        temp_operand[i], temp_operand[i+1], each_op)
                    # temp_operand.insert(i, res)
                    temp_operand[i+1] = res

        ans.append(abs(temp_operand[0]))
    return max(ans)


def sort_out_ops(operator):
    res = []
    if '*' in operator:
        res.append('*')
    if '-' in operator:
        res.append('-')
    if '+' in operator:
        res.append('+')
    return res

# 50 * 6 - 3 * 2

# 50 6 3 2
# * - *

# i=0: 300 3 2

# * -
# - *

    #     i = 0
    #     print(each_operator_set)
    #     # break
    #     while len(temp_operand) != 1:
    #         operand1 = temp_operand.popleft()
    #         operand2 = temp_operand.popleft()
    #         op = each_operator_set[i]
    #         i += 1

    #         res = apply_ops(operand1, operand2, op)
    #         temp_operand.insert(0, res)
    #     ans.append(abs(temp_operand[0]))
    # return max(ans)


def seperate_ops(exp: str):
    operand = []
    operator = []
    temp = ""
    for each in exp:
        if each in "*+-":
            operator.append(each)
            operand.append(int(temp))
            temp = ""
        else:
            temp += each
    # the last remaining operand
    operand.append(int(temp))
    return operand, operator


def apply_ops(operand1, operand2, operator):
    if operator == '*':
        return operand1 * operand2
    elif operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2


# expression1 = "100-200*300-500+20"
expression2 = "50*6-3*2"
result1 = 60420
result2 = 300

# print(solution(expression1), result1)
print(solution(expression2), result2)

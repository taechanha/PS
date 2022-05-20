from itertools import permutations as P


def solution(expression):
    max_res = -float('inf')

    e = expression.replace('*', ':')
    e = e.replace('-', ':')
    e = e.replace('+', ':')
    operands: list = e.split(':')
    operators = []
    # 연산자 우선순위 정하기; 종류 개수에 따라 결정됨: 1->1, 2->2, 3->6
    for exp in expression:
        if exp in ('*', '+', '-'):
            operators.append(exp)

    cases = list(P(set(operators)))
    for case in cases:
        temp_operands = operands[:]
        temp_operators = operators[:]
        for prior_op in case:
            # 현재 op가 그 어떤 다른 op보다 우선순위가 높음 -> 먼저 처리
            # 순서는? 50*6-3*2, 식의 형식에 따라, 피연산자-연산자-피연산자 탐색 후 계산결과를 왼쪽에 append
            i = 0
            while i < len(temp_operators):
                if temp_operators[i] == prior_op:
                    lhs = temp_operands.pop(i)
                    rhs = temp_operands.pop(i)
                    temp_operands.insert(i, str(eval(lhs + prior_op + rhs)))
                    temp_operators.pop(i)
                else:
                    i += 1

        res = abs(int(temp_operands[0]))
        max_res = max(max_res, res)

    return max_res


expression = "50*6-3*2"  # "100-200*300-500+20"  #
res = solution(expression)
print(res)

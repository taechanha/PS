# 6
# 1 2 3 4 5 6
# 2 1 1 1
n = 0
def rec(k, result):
    if k == n-1:
        min_res = min(min_res, result)
        max_res = max(max_res, result)
    
    for cand in range(4):
        if operators[cand] >= 1:
            operators[cand] -= 1
            result = calculate(result, cand, operand[k+1])
            rec(k+1, result)
            operators[cand] += 1
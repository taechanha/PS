from itertools import permutations
from collections import deque

n = int(input())
operands = deque(map(int, input().split()))
# 덧 뺄 곱 나
add, sub, mul, div = map(int, input().split())

def get_ops():
    op_list = ['+' for _ in range(add)]
    op_list += ['-' for _ in range(sub)]
    op_list += ['*' for _ in range(mul)]
    op_list += ['/' for _ in range(div)]

    return set(permutations(op_list))

def cal(x, y, op):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: -(abs(x) // y) if x < 0 else x // y
    }
    return ops[op](x, y)

ops_list = get_ops()

max_val = -float('inf')
min_val = float('inf')
for ops in ops_list:
    temp_operands = operands.copy()
    for op in ops:
        a, b = temp_operands.popleft(), temp_operands.popleft()
        res = cal(a, b, op)
        temp_operands.appendleft(res)
    max_val = max(max_val, temp_operands[0])
    min_val = min(min_val, temp_operands[0])

print(max_val)
print(min_val)

stack1 = list(input())
stack2 = []
t = int(input())
cur = len(stack1) - 1
while t:
    t -= 1

    inst = list(input().split())
    # [a,b,c] [d,e]
    if len(inst) == 1:  # L, D, B
        if inst[0] == 'L':
            if len(stack1) == 0:
                continue
            stack2.append(stack1.pop())
        elif inst[0] == 'D':
            if len(stack2) == 0:
                continue
            stack1.append(stack2.pop())
        else:  # B
            if len(stack1) == 0:
                continue
            stack1.pop()
    else:  # P $
        stack1.append(inst[1])

print(''.join(stack1 + stack2[::-1]))

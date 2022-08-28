
def run(inst):
    error = 0
    if inst[0] == "NUM":
        stack.append(inst[1])
    if inst[0] == "POP":
        if len(stack) == 0:
            error = 1
            return
        stack.pop()
    if inst[0] == "INV":
        stack[-1] = -stack[-1]
    if inst[0] == "DUP":
        if len(stack) == 0:
            error = 1
            return
        stack.append(stack[-1])
    if inst[0] == "SWP":
        if len(stack) <= 1:
            error = 1
            return
        last = stack.pop()
        sec_last = stack.pop()
        stack.append(sec_last)
        stack.append(last)
    if inst[0] == "ADD":
        if len(stack) <= 1:
            error = 1
            return
        last = stack.pop()
        sec_last = stack.pop()
        stack.append(sec_last + last)
    if inst[0] == "SUB":
        if len(stack) <= 1:
            error = 1
            return
        last = stack.pop()
        sec_last = stack.pop()
        stack.append(sec_last - last)
    if inst[0] == "MUL":
        if len(stack) <= 1:
            error = 1
            return
        last = stack.pop()
        sec_last = stack.pop()
        stack.append(sec_last * last)
    if inst[0] == "DIV":
        if len(stack) <= 1:
            error = 1
            return
        last = stack.pop()
        sec_last = stack.pop()
        if not (last < 0 and sec_last < 0):
            if last < 0 or sec_last < 0:
                flag = 1
        if flag == 1:
            stack.append(-(sec_last / last))
        else:
            stack.append(sec_last / last)
    if inst[0] == "MOD":
        if len(stack) <= 1:
            error = 1
            return
        last = stack.pop()
        sec_last = stack.pop()
        if not (last < 0 and sec_last < 0):
            if last < 0 or sec_last < 0:
                flag = 1
        if flag == 1:
            stack.append(-(sec_last % last))
        else:
            stack.append(sec_last % last)

    return error


stack = []
prog = []
data = []

cur = input().split()
while cur[0] != "QUIT":
    while cur[0] != "END":
        prog.append(cur)
        cur = input().split()

    n = int(input())
    data = [int(input()) for _ in range(n)]

    for i in range(n):
        stack = []
        for inst in prog:
            error = run(inst)
        if error != 1:
            print(stack[-1])
        elif error == 1 or len(stack) != 1:
            print("ERROR")

#test = "([]())"
#test = "(]"
#test = "([)]"
#test = "[ ([]) () (()) ]"
debug = 0
while True:
    if debug:
        si = test
    else:
        si = input()
    if si[0] == '.':
        break

    p_open = 0
    s_open = 0
    prev = []
    fl = 0
    for each in si:
        if each == '(':
            p_open += 1
        elif each == ')':
            if p_open > 0 and prev and prev.pop() == '(':
                p_open -= 1
            else:
                fl = 1
        elif each == '[':
            s_open += 1
        elif each == ']':
            if s_open > 0 and prev and prev.pop() == '[':
                s_open -= 1
            else:
                fl = 1
        # caution; do not forget
        if each in '([':
            prev.append(each)

    # fl == 1만 체크했음. 이 실수를 어떻게 반복하지 않을까? 수도코드 먼저 작성하고, 수도코드를 수정하면, 정답을 내는 코드에도 수정이 필요한지 확인한다. malloc free와 같이 한 쌍이라 생각하자.
    if fl == 1 or p_open > 0 or s_open > 0:
        print("no")
    else:
        print("yes")

    if debug:
        break

from curses.ascii import isalnum


t = int(input())

while t:
    t -= 1

    s = list(input())
    stack1 = []
    stack2 = []

    for i in range(len(s)):
        each = s[i]
        if each == '<':         # <
            if len(stack1) == 0:
                continue
            stack2.append(stack1.pop())
        elif each == '>':       # >
            if len(stack2) == 0:
                continue
            stack1.append(stack2.pop())
        elif each.isalnum():    # isalpha() or isnum()
            stack1.append(each)
        else:                   # -
            if len(stack1) == 0:
                continue
            stack1.pop()

    print("\n" + ''.join(stack1 + stack2[::-1]))  # 뒤에거 뒤집는거 잊지말자 제발 ㅠㅠㅠㅠㅠㅠㅠㅠㅠ

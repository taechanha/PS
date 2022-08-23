# 2:25 ~ 2:37

t = int(input())
while t:
    t -= 1

    n = int(input())
    string = input().split()
    pipe = [string[0]]

    for each in string[1:]:
        # greedy
        # 1. pipe의 front ptr 값보다 같거나 작다면
        if each <= pipe[0]:
            pipe.insert(0, each)
        # 2. 크다면
        else:
            pipe.append(each)

    print(''.join(pipe))

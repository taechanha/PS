
t = int(input())

while t:
    t -= 1

    s = input()

    keys = []
    flag = 0
    for each in s:
        if each in "rgb":
            keys.append(each)
        else:
            if each.lower() not in keys:
                flag = 1
                break
    if flag == 1:
        print("NO")
    else:
        print("YES")

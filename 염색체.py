def count_in_cond(s):
    cnt = 0
    for each in s:
        if each in cond:
            cnt += 1
    return cnt


def is_there(s, char):
    return char in s


n = int(input())
cond = ["A", "B", "C", "D", "E", "F"]
while n:
    n -= 1
    s = input()
    i = 0

    if len(s) < 3:
        print("Infected!")
        continue

    if is_there(s, 'A'):
        i = s.index('A')
    else:
        print("Good")
        continue
    if is_there(s[i:], 'F'):
        i = i + s[i:].index('F')
    else:
        print("Good")
        continue
    if is_there(s[i:], 'C'):
        i = i + s[i:].index('C')
    else:
        print("Good")
        continue

    #    i = 6, len(s) = 7
    # [... C]
    # at the end
    if i + 1 == len(s):
        print("Infected!")
        continue
    else:
        # len(s) > i + 1
        # s[i + 1] possible
        if s[i + 1] not in cond:
            print("Good")
            continue
        else:   # i = 6, s[i + 1] = 'B' , len(s) = 7
            # cond 중 1개 이상 있는 상태
            # 더 이상의 문자는 없어야 함
            if i + 2 <= len(s):
                print("Good")
                continue
    print("Infected!")
# 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
# 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한

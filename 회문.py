from distutils.command.build_scripts import first_line_re


def is_palindrome(s):
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
        if s[p1] == s[p2]:
            p1 += 1
            p2 -= 1
        else:
            return False
    return True


def is_pseudo_palindrome(s):
    p1 = 0
    p2 = len(s) - 1

    cnt1 = cnt2 = 1
    first_bool = sec_bool = True
    while p1 < p2:
        if s[p1] == s[p2]:
            p1 += 1
            p2 -= 1
        elif cnt1 == 1:
            p1 += 1
            cnt1 -= 1
        else:
            first_bool = False
            break

    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if s[p1] == s[p2]:
            p1 += 1
            p2 -= 1
        elif cnt2 == 1:
            p2 -= 1
            cnt2 -= 1
        else:
            sec_bool = False
            break

    if first_bool or sec_bool:
        return 1
    else:
        return 0


# def is_pseudo_palindrome(s):
#     temp_s = s
#     for i in range(len(s)):
#         temp_s = s[:i] + s[i + 1:]
#         if is_palindrome(temp_s):
#             return True
#     return False


n = int(input())
while n:
    n -= 1
    s = input()
    if is_palindrome(s):
        print(0)
    elif is_pseudo_palindrome(s) == 1:
        print(1)
    else:
        print(2)

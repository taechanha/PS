def remove_num(s: str):
    temp = ""
    for each in s:
        if not each.isdigit():
            temp += each
    return temp


def is_matching(s: str, kw: str):
    if s == kw:
        return True

    for i in range(len(s) - len(kw) + 1):
        if s[i:i+len(kw)] == kw:
            return True
    return False


si = input()
kw = input()

si = remove_num(si)

if is_matching(si, kw):
    print(1)
else:
    print(0)

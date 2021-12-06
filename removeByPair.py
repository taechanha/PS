def solution(s):
    i = 0
    len_s = len(s)
    s = list(s)
    while s and i < len_s - 1:
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i = 0
            len_s = len(s)
            continue

        i += 1
        len_s = len(s)

    return s == []


solution("baabaa")

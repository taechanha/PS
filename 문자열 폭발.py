# mirkovC4nizCC44
# C4


def solution(s: str, t: str):
    n = len(t)
    while s and t in s:
        i = s.find(t)
        s = s[:i] + s[i+n:]

    if not s:
        return "FRULA"

    return s


# s = "mirkovC4nizCC44"
# t = "C4"
# s = "12ab112ab2ab"
# t = "12ab"
s = input()
t = input()
res = solution(s, t)
print(res)

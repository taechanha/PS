
def validate(string):
    is_underscore, is_uppercase = False, False
    if string[0].isupper():  # java 위배
        return False
    if string[0] == '_':  # cpp 위배
        return False
    if string[-1] == '_':  # cpp 위배
        return False
    prev = None
    for ch in string:
        if prev and ch == prev and prev == '_':  # cpp 위배
            return False
        if ch == '_':
            is_underscore = True
        elif ch.isupper():
            is_uppercase = True
        prev = ch
    if is_underscore and is_uppercase:  # java, cpp 모두 만족하는 형식 -> 위배
        return False


def is_cpp_or_java(string):
    cpp, java = False, False
    for ch in string:
        if ch == '_':  # c++
            cpp = True
            return True, True
        elif ch.isupper():  # java
            java = True
            return True, False
    if not cpp and not java:
        return False, None


def process_string(string, cpp):
    flag = False
    answer = ""
    if cpp:
        for ch in string:
            if ch == '_':
                flag = True
                continue
            if flag:
                answer += ch.upper()
                flag = False
            else:
                answer += ch
    else:
        for ch in string:
            if ch.isupper():
                answer += '_' + ch.lower()
            else:
                answer += ch
    return answer


def solution(string):
    ERROR = "Error!"

    if validate(string) == False:  # invalid
        return ERROR

    either, cpp = is_cpp_or_java(string)  # c++ or java
    if either == False:
        return string

    answer = process_string(string, cpp)
    return answer


if __name__ == "__main__":
    string = input()
    answer = solution(string)
    print(answer)

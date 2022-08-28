stack = []
table = {
    ')': '(',
    '}': '{',
    ']': '['
}


def validParentheses(s: str):
    for char in s:
        if char not in table:
            stack.append(char)
        elif stack and table[char] != stack.pop():
            return False
    return True


s = "{}()[]"
s = "{{{}}}"
print(validParentheses(s))

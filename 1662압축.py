# 6:13 ~ 6:41

s = input()
length = 0
cnt = ''
stack = []
for c in s:
    if c.isdigit():
        length += 1
        cnt = c
    elif c == '(':
        stack.append((cnt, length-1))
        length = 0
    elif c == ')':
        cnt, curr_len = stack.pop()
        cnt = int(cnt)
        length = (length * cnt) + curr_len
print(length)

# 33(562(71(9)))
# [(3, 1), (2, 2), (1, 1)]


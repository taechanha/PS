# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx

def left_fill(s: str, diff: int):
    return s + ('#' * diff)


t = 5
s = []

while t:
    s.append(input())
    t -= 1

max_len = max([len(x) for x in s])

# fill rest as #
for i in range(len(s)):
    diff = max_len - len(s[i])
    s[i] = left_fill(s[i], diff)

print(s)
# print as the mentioned format
for i in range(len(s[0])):
    for j in range(len(s)):
        if s[j][i] == '#':
            continue
        print(s[j][i], end='')

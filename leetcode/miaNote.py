def join(s1, s2):
    if s1 == '?':
        return s2
    else:
        return s1


def filter_dup(s):
    s = set(s)
    return sorted(s)[-1]


n, h, w = map(int, input().split())
s = []

for i in range(h):
    s.append(input().split()[0])

s = [[char for char in line] for line in s]

for i in range(1, h):
    for j in range(len(s[0])):
        s[i][j] = join(s[i-1][j], s[i][j])

answer = ""
for i in range(0, len(s[0]), w):  # 0, w, w*2, ...
    answer += filter_dup(s[-1][i:i+w])

print(answer)

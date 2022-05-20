# 12:17 ~ 1:00 (failed ~)

# 제일 많이 겹치는 substring

def get_substr(base):
    n = len(base)
    substrs = []
    for i in range(n):
        for j in range(i, n):
            substrs.append((i, base[i:j+1]))
    return substrs


base = "xy0z"
target = "zzz0yyy0xxx"
n = len(base)
m = len(target)

# 각 문자열의 substring을 구하고, 큰 순으로 정렬, 겹치는 게 있다면 target에서 제외

base_substr = get_substr(base)
base_substr.sort(key=lambda x: -len(x[1]))
cnt = 0
while target:

    target_substr = get_substr(target)

    target_substr.sort(key=lambda x: -len(x[1]))

    substr, index = [], []
    for i, s in target_substr:
        index.append(i)
        substr.append(s)

    flag = 0
    for _, b in base_substr:
        try:
            i = substr.index(b)
            i = index[i]
            target = target[:i] + target[len(b)+1:]
            break
        except:
            pass

    cnt += 1

print(cnt)

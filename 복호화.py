from collections import defaultdict


def most_common(counter: dict):  # 정렬되어있다는 가정
    ret = []
    max_count = 0
    for k, v in counter.items():
        if v >= max_count:
            max_count = v
            ret.append(k)
    return ret


t = int(input())
while t:
    counter = defaultdict(int)
    for ch in input():
        if ch == ' ':
            continue
        counter[ch] += 1

    counter = {k: v for k, v in sorted(counter.items(), key=lambda x: -x[1])}
    most_commons = most_common(counter)

    if len(most_commons) > 1:
        print("?")
    else:
        print(*most_commons)

    t -= 1

# 3
# 3 1 2
# 3 1 1
# 3 1 3

from itertools import permutations as P


def get_all_substr(s):
    substr = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr.append(s[i:j])
    return substr


T = int(input())
i = 0

while i < T:
    i += 1

    n, a, b = map(int, input().split())

    each = Range = range(1, n+1)

    substr = get_all_substr(list(range(1, n+1)))

    substr.sort(key=lambda x: len(x))

    data = set(range(1, n+1))
    flag = 0
    for each in substr:
        A = sum(each)
        B = sum(data - set(each))

        if (B != 0 and (A / B) == (a / b)) or (A != 0 and (B / A) == (a / b)):
            print(f"Case #{i}:", "POSSIBLE")
            print(len(each))
            print(*each)
            flag = 1
            break
    if not flag:
        print(f"Case #{i}:", "IMPOSSIBLE")

    # flag = 0
    # # for each in P(Range):
    # for k in range(len(each)):
    #     A = sum(each[:k])
    #     B = sum(each[k:])

    #     if (B != 0 and (A / B) == (a / b)) or (A != 0 and (B / A) == (a / b)):
    #         print(f"Case #{i}: ", "POSSIBLE")
    #         print(k)
    #         print(' '.join(map(str, each[:k])))
    #         flag = 1
    #         break
    # # if flag:
    #         # break
    # if not flag:
    #     print(f"Case #{i}: ", "IMPOSSIBLE")

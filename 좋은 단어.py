# 위로 아치를 만들어 겹치지 않으면..
#   -> 인접한 pair 삭제?
#   -> 언제까지?
#      - 글자가 2개 미만으로 남으면 종료
#      - one pass에 삭제되는 페어가 없으면 종료

N = int(input())
strings = [input() for _ in range(N)]
good_words = 0

for s in strings:
    step = 0
    idxs = []
    if len(s) % 2 != 0:
        continue
    while True:
        # 1
        archies = 0
        flag = 0

        # 2
        if step >= 1:
            new_s = ""
            for idx in idxs:
                new_s += s[idx]

            if s == new_s:
                break
            s = new_s

        LEN = len(s)
        idxs = []
        # 3
        for i in range(LEN):
            if flag == 1:
                flag = 0
                continue

            if i < LEN-1 and s[i] == s[i+1]:
                flag = 1
                archies += 1
            else:
                idxs.append(i)

        # termination condition
        if len(idxs) == 0:
            if archies == LEN // 2:
                good_words += 1
                break
        else:
            if archies == 0:
                break


        step += 1

print(good_words)


# res = 0
# for i in range(int(input())):
#     s = input()
#     stack = ['']
#     for c in s:
#         if stack[-1] == c:
#             stack.pop()
#         else:
#             stack.append(c)
#     if len(stack) == 1:
#         res+= 1
# print(res)
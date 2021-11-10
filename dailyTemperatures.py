# def dailyTemperatures(temperatures):
#     answer = []
#     for i in range(len(temperatures)-1):
#         j = i + 1
#         while temperatures[i] >= temperatures[j]:
#             j += 1

#             if j == len(temperatures):
#                 j = i
#                 break

#         answer.append(j - i)

#     return answer + [0]

def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


T = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(T))

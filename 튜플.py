# [[1], [1, 2] ...] 꼴로 만들기
# 결과 리스트에서 각각을 길이 별로 정렬
# 길이 순서대로 ans에 없는 요소만 추가
# return ans

def solution(s):
    answer = []

    res = preprocess(s)
    print(res)
    res.sort(key=lambda x: len(x))
    print(res)

    for i in range(len(res)):
        for j in range(len(res[i])):
            if res[i][j] not in answer:
                answer.append(res[i][j])
    print(answer)
    return answer


def preprocess(s):
    s = s[2:-2].split('},{')
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))
    return s


# def preprocess(s: str):
#     res = s.split('{')
#     res = ''.join(res)
#     res = res.split('}')
#     ans = []
#     for each in res:
#         new = []
#         atom = ''
#         if each == '':
#             continue
#         for i in range(len(each)):
#             if each[i].isdigit():
#                 atom += each[i]
#             else:
#                 if atom != '':
#                     new.append(atom)
#                     atom = ''

#         if atom != ',':
#             new.append(atom)
#         ans.append(new)

#     for i in range(len(ans)):
#         for j in range(len(ans[i])):
#             ans[i][j] = int(ans[i][j])

#     return ans


test = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
test = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
test = "{{20,111},{111}}"
test = "{{123}}"
test = "{{4,2,3},{3},{2,3,4,1},{2,3}}"


print(solution(test))

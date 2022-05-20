# def solution(sentences, n):
#     answer = 0

#     for sentence in sentences:
#         score = len(sentence) - 1  # 공백을 제외한 문자 갯수.

#         # 첫번째 문자가 대문자일 경우 shift + lowercase_letter 이다.
#         if sentence[0].isupper():
#             score += 1

#         # 2~n-1번 index의 문자들을 탐험한다. (shift + letter or spacebar + letter)
#         for i in range(1, len(sentence)):
#             # upper case & previous character is not a space bar -> shift key needed! (+2 keys used.)
#             if sentence[i].isupper() and not sentence[i-1] == ' ':
#                 score += 2

#         if score <= n:  # the number of available keys >= the number of required keys to complete this string? then add it to the total points! :)
#             answer += len(sentence) - 1

#     return answer

# def solution(sentences, n):
#     answer = 0

#     for sentence in sentences:
#         score = 0
#         for i in range(len(sentence)):
#             # 대문자일 경우 소문자로 변환해서 점수 계산. shift + lowercase_letter이다.
#             if sentence[i].isupper():
#                 # a~z : 97~122, A~Z : 65~90 (ord() : ascii code return)
#                 score += 1 + ord(sentence[i].lower()) - ord('a')

#             else:  # 소문자일 경우 그냥 점수 계산. lowercase_letter이다.
#                 score += ord(sentence[i]) - ord('a')

#         # spacebar 빼고 n keys available한다. -> len([c for c in sentence if c != ' ']) <= n (spacebar 빼고 string length) -> complete the string! -> get points equal to the length of the completed string! (score)
#         if len([c for c in sentence if c != ' ']) <= n:
#             answer = max(answer, score)

#     return answer

def solution(sentences, n):
    answer = 0

    for sentence in sentences:
        score = 0
        for i in range(len(sentence)):
            # 대문자일 경우 소문자로 변환해서 점수 계산. shift + 소문자이니까 2개.
            if sentence[i].isupper():
                # ord() : 문자 -> 아스키 코드, chr() : 아스키 -> 문자. a=97, A=65. lower() : 모두 소문자 / upper() : 모두 대문ㅇㅣㅇ / capitalize() : 1st letter to uppercase / title() : every first letter to uppercase.
                score += ord(sentence[i].lower()) - 96 + 2

            else:  # 그 외의 경우 점수 계산.
                score += ord(sentence[i]) - 96

            if i == n:  # 문자를 완성하는 경우, 다음 문자로 넘김.
                break

        answer = max(answer, score)  # 최대 점수 계산.

    return answer

# def solution(sentences, n):
#     answer = 0

#     for sentence in sentences:
#         score = 0
#         for i in range(len(sentence)):
#             # 대문자일 경우 소문자로 변환해서 점수 계산. shift + 소문자이다.
#             if sentence[i].isupper():
#                 # ord() : 문자 -> ASCII code, chr() : ASCII code -> 문자. a=97, A=65, z=122, Z=90
#                 score += ord(sentence[i].lower()) - 96 + 1

#             # 소문자일 경우 그냥 정해둔 n+1의 key set을 활당할 수 없다. (shift + key set) => 2n+1 keyset. (n+1)*2-1 = 2n-1 keyset. => n keyset can't use this case! so we need to minus 1 from the score!
#             else:
#                 # ord() : 문자 -> ASCII code, chr() : ASCII code -> 문자. a=97, A=65, z=122, Z=90
#                 if ord(sentence[i]) - 96 > n:
#                     score -= 1

#             if i == len(sentence) - 1:  # 마지막 글자일 경우 점수 +1 (spacebar)
#                 score += 1
#         print(score)
#         answer = max(answer, score)

#     return answer


sentences = ["line in line", "LINE", "in lion"]
n = 5
# sentences = ["ABcD", "bdbc", "a", "Line neWs"]
# n = 7

res = solution(sentences, n)
print(res)


# 부서진 키보드가 있습니다. 부서진 키보드는 공백을 입력하기 위한 스페이스바와 스페이스바 외의 다른 n개의 키만 사용이 가능합니다.
# 예를 들어 n이 4고 l, i, n, e 4개의 키를 사용할 수 있다고 했을 때, "line in line", "in    n          in"과 같은 문장을 만들 수 있습니다.
# 알파벳 대문자를 만들려면 shift키와 해당 알파벳의 소문자 키가 필요합니다.
# 예를 들어, "L I N e"을 완성하려면 shift, l, i, n, e 이렇게 5개의 키가 필요합니다.

# 당신은 이 부서진 키보드로 주어진 문자열 배열에 있는 문자열을 완성하면 완성한 문자열의 길이만큼 점수를 받는 게임을 하려고 합니다.
# 예를 들어, "coding is fun"이라는 문자열을 완성하면 13점을 얻을 수 있습니다.
# 단, 완성된 문자열 속에 알파벳 대문자가 있을 경우 알파벳 대문자 개수만큼 1점씩 추가로 점수를 얻을 수 있습니다.
# 예를 들어, "COding is fun"이라는 문자열을 완성하면 15(= 13 + 2)점을 얻을 수 있습니다.
# 문자열을 완전히 완성시키지 못하면 점수를 얻을 수 없습니다.
# 예를 들어, "abcde"라는 문자열을 "abc"까지만 완성하면 점수를 얻을 수 없습니다.

# 여러 개의 문자열을 담은 문자열 배열 sentences와 스페이스바 외에 사용 가능한 키의 개수를 나타내는 정수 n이 매개변수로 주어집니다. 이때, 얻을 수 있는 최대 점수를 return 하도록 solution 함수를 완성해주세요. 단, 완성할 수 있는 문자열이 없을 경우 0을 return 해주세요.

# 제한사항
# 1 ≤ sentences 길이 ≤ 15
# 1 ≤ sentences의 원소 길이 ≤ 100,000
# sentences의 원소는 알파벳과 공백으로 이루어져 있습니다.
# sentences의 원소는 항상 알파벳으로 시작하여 알파벳으로 끝납니다.
# 예를 들어, ["a ", " A ", " A"]와 같은 원소는 주어지지 않습니다.
# 1 ≤ n ≤ 27
# 입출력 예
# sentences	n	result
# ["line in line", "LINE", "in lion"]	5	20
# ["ABcD", "bdbc", "a", "Line neWs"]	7	12
# 입출력 예 설명
# 입출력 예 #1

# 문자열	필요한 키	점수
# "line in line"	l, i, n, e	12
# "LINE"	shift, l, i, n, e	8
# "in lion"	l, i, n, o	7
# 사용할 키로 l, i, n, e, o를 고르면 첫 번째와 세 번째 문자열을 완성해 19점을 얻을 수 있습니다.
# 하지만, l, i, n, e, shift를 고르면 첫 번째와 두 번째 문자열을 완성해 20점을 얻을 수 있습니다.
# 따라서 20을 return 해야 합니다.

# 입출력 예 #2

# 문자열	필요한 키	점수
# "ABcD"	shift, a, b, c, d	7
# "bdbc"	b, c, d	4
# "a"	a	1
# "Line neWs"	shift, l, i, n, e, w, s	11
# 사용할 키로 shift, l, i, n, e, w, s를 고르면 네 번째 문자열을 완성해 11점을 얻을 수 있습니다.
# 하지만, shift, a, b, c, d를 고르면 첫 번째, 두 번째, 세 번째 문자열을 완성해 12점을 얻을 수 있습니다. (7개까지 키를 사용할 수 있지만 5개로도 충분히 3개의 문자열을 완성할 수 있습니다.)
# 따라서 12를 return 해야 합니다.
# def removeDuplicateLetters(s):

#     # 집합으로 정렬
#     for i, char in enumerate(sorted(set(s))):
#         suffix = s[s.index(char):]
#         #print(char, suffix, i)

#         #print(set(s), set(suffix))
#         # 전체 집합과 접미사 집합이 일치할 때 분리
#         if set(s) == set(suffix):
#             return char + removeDuplicateLetters(suffix.replace(char, ''))

#     return ''


import collections


def removeDuplicateLetters(s):
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return ''.join(stack)


removeDuplicateLetters("cbacdcbc")

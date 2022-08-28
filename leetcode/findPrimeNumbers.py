# from itertools import permutations


# def solution(numbers):
#     s = set()
#     for i in range(1, len(numbers)+1):
#         tmp = ""
#         for j in permutations(numbers, i):
#             s.add(int("".join(list(j))))
#     cnt = 0
#     for elem in s:
#         if is_prime(elem):
#             cnt += 1
#     return cnt


# def is_prime(n):
#     n = abs(int(n))
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if not n & 1:
#         return False
#     for x in range(3, int(n**0.5) + 1, 2):
#         if n % x == 0:
#             return False
#     return True


# A
# AA
# AAA

# AAAA  : 4
# AAAAA
# AAAAE
# AAAAI
# AAAAO
# AAAAU

# AAAE  : 10
# AAAEA        # tofind: AAAAE
# AAAEE
# AAAEI
# AAAEO
# AAAEU
# AAAI  : 16
# lex = "AEIOU"
# nth = 0


# def helper(word, tofind):
#     global nth
#     if word == tofind:
#         return -1
#     if len(word) == 5:
#         return
#     else:
#         for i in range(5):
#             # choose
#             word += lex[i]
#             # explore
#             nth += 1
#             found = helper(word, tofind)
#             if found == -1:
#                 break
#             # un-choose
#             word = word[:-1]
#     return found


# def solution(word):
#     helper("", word)
#     global nth
#     return nth

from itertools import product


def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer


print(solution("AAAI"))

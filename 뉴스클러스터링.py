# 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면,
# 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로,
# 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

# preprocess:
#   1. upper()
#   2. 두 글자씩 끊기: FRAN -> FR RA AN
#   3. 숫자, 공백, 특수문자 포함된 경우 "그 쌍" 날리기: ab  -> a, ab3 ->  ab+ -> a

# 2, 3

def seperate_by_two(s):
    temp = []
    for i in range(len(s) - 1):
        if s[i].isalpha() and s[i+1].isalpha():
            concat = s[i] + s[i+1]
            temp.append(concat)
            # temp.append(concat + str(temp.count(concat[::-1])))
            # Ex. now, temp would be [FR1, RA2]
    # print()
    for i in range(len(temp)-1, -1, -1):
        # print(temp[i])
        temp[i] += str(temp.count(temp[i]))
    return set(temp)


def solution(str1, str2):
    # 1
    str1 = str1.upper()
    str2 = str2.upper()

    s1 = seperate_by_two(str1)
    s2 = seperate_by_two(str2)

    #print(s1, s2)

    #str1: aa1+aa2
    #str2: AAAA12
    # s1: {aa, a1, 1+, +a, aa, a2} -> {aa, aa}      -> {aa1, aa2}
    # s2: {aa, aa, aa, a1, 12}     -> {aa, aa, aa}  -> {aa1, aa2, aa3}

    # 교/합집합 구할 때, 다중집합 개념을 적용해야함 => 각 아이템 당 id를 먹여주면 그냥 집합 api 써서 해결 가능
    # 교집합

    # return
    intersection = s1.intersection(s2)
    # 합집합
    union = s1.union(s2)

    # return 65536 if s2(분모) is empty

    # case1: "aa" "" -> s1 = {aa}, s2 = {}, intersection = {}, union = {aa} => ans = 0 -> OK
    # case2: "" "aa" -> s1 = {}, s2 = {aa}, intersection = {}, union = {aa} => ans = 0 -> OK 
    if not union:
        return 65536
    ans = len(intersection) / len(union)
    return int(ans * 65536)

# test cases #

str1 = "aa1+aa2"
str2 = "AAAA12"

str1 = "FRANCE"
str2 = "french"

str1 = "handshake"
str2 = "shake hands"

str1 = "E=M*C^2"
str2 = "e=m*c^2"

# print answer
res = solution(str1, str2)
print(res)

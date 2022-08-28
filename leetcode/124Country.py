def solution(n):
    scope = ['1', '2', '4']
    answer = ""
    while n:
        # n = (n-1) // 3
        n, r = divmod(n-1, 3)
        answer = scope[r] + answer
    return answer


# scope[(((n//3)//3)%3)] + scope[(n//3)%3] + scope[n % 3]

# 10진수 -> 3진수 변환과의 차이
# 3진수 변환 코드
# while n:
#     n, r = divmod(n, 3)
#     answer = str(r) + answer
# return answer

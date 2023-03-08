start = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
end = "라고 답변하였지."
base = '"재귀함수는 자기 자신을 호출하는 함수라네"'
prompt1 = '"재귀함수가 뭔가요?"'
prompt2 = "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
prompt3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
prompt4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
level = "____"


def print_rec(n):
    print(level*(N-n) + prompt1)
    if n == 0:
        print(level*(N-n) + base)
        print(level*(N-n) + end)
        return

    print(level*(N-n) + '"' + prompt2)
    print(level*(N-n) + prompt3)
    print(level*(N-n) + prompt4 + '"')
    print_rec(n-1)
    print(level*(N-n) + end)


N = int(input())
print(start)
print_rec(N)

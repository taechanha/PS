from functools import cmp_to_key


def ext_head(x):
    head_x = ""
    for i in range(len(x)):
        if x[i].isdigit():
            break
        head_x += x[i]
    return head_x, i


def ext_num(x, i):
    x = x[i:]
    num_x = ""
    for j in range(len(x)):
        if not x[j].isdigit():
            break
        num_x += x[j]
    return num_x, i + j


def ext_tail(x, i):
    return x[i:]


def cmp(x, y):
    # 영문 대/소문자, 숫자, 공백, 마침표, 빼기 부호
    """ foo9.txt """

    # 1. HEAD, NUMBER, TAIL로 분리 | 숫자 전까지가 헤드, 숫자 중이 숫자, 숫자 후가 테일일듯
    headx, i = ext_head(x)
    numx, i = ext_num(x, i)
    tailx = ext_tail(x, i)

    heady, i = ext_head(y)
    numy, i = ext_num(y, i)
    taily = ext_tail(y, i)

    # 2. HEAD 부분으로 사전 순 정렬, 대소문자 구분 X
    # 3. NUMBER 숫자 순으로 정렬, 숫자 앞의 0은 무시 Ex. 012 -> 12
    headx = headx.upper()
    heady = heady.upper()
    if headx > heady:
        return 1
    elif headx == heady:
        if int(numx) > int(numy):
            return 1
        elif int(numx) == int(numy):
            return 0
        else:
            return -1
    else:
        return -1


def solution(files):

    srt = sorted(files, key=cmp_to_key(cmp))

    return srt


files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]
files = ["F-5 Freedom Fighter", "B-50 Superfortress",
         "A-10 Thunderbolt II", "F-14 Tomcat"]
res = solution(files)
print(res)

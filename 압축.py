from string import ascii_letters


def init():
    """
    return: dict, int
    """
    d = dict()
    idx = 0
    for c in ascii_letters:
        if c.islower():
            continue
        idx += 1
        d[c] = idx
    return d, idx


def solution(msg) -> list[int]:
    ans = []

    # 1. init dict of upper alpha
    lex, idx = init()

    # 2. msg와 일치하는 가장 긴 문자열 w를 lex에서 찾기
    i = 0
    while i < len(msg):
        for ri in range(len(msg), i, -1):
            # "KAKAO", "KAKA", "KAK", ... "K"
            #   2-2. 없으면, 찾을 때까지 w의 크기를 줄여나감
            w = msg[i:ri]
            if w in lex:
                ans.append(lex[w])
                break
        # print(msg, ri, w)

        # 3. 입력에서 처리되지 않은 글자가 있으면 w+c에 해당하는 단어 사전에 등록
        #   Ex. msg: KAO | KA 존재 | 처리되지 않은 글자 O => KAO를 사전에 등록
        if ri != len(msg):
            w_c = w + msg[ri]
            idx += 1
            lex[w_c] = idx

        #   2-1. 있으면, 인덱스 번호 출력하고, 입력에서 w 제거
        i += len(w)
        #msg = msg[i:]
    return ans


msg1 = "KAKAO"
ans1 = [11, 1, 27, 15]
msg2 = "TOBEORNOTTOBEORTOBEORNOT"
ans2 = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
msg3 = "ABABABABABABABAB"
ans3 = [1, 2, 27, 29, 28, 31, 30]

print(ans1 == solution(msg1))
print(ans2 == solution(msg2))
print(ans3 == solution(msg3))


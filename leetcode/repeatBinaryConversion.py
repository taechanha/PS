def solution(s):
    cnt = 0
    i = 0
    while s != "1":
        answer = ""
        i += 1
        for x in s:
            if x == "0":
                cnt += 1
            else:
                answer += x
        s = bin(len(answer))[2:]

    return [i, cnt]

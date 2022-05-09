N=3
M=2

selected = [0] * (M+1)
def rec(k: int):
    if (k == M + 1):
        # selected[1...M] 배열이 새롭게 탐색된 결과
        sb = []
        for i in range(1, M+1):
            sb.append(str(selected[i]) + ' ')
        print(sb)
    else:
        for cand in range(1, N+1):
            # k번째에 cand가 올 수 있으면
            selected[k] = cand

            # k+1번 부터 M번까지 잘 채워주는 함수를 호출해준다.
            rec(k+1)
            selected[k] = 0

rec(1)


############################

N=3
M=2
def rec(i, chosen):
    if len(chosen) >= M:
        print(chosen)
        return

    for i in range(1, N+1):
        chosen.append(i)
        rec(i, chosen)
        chosen.pop()
rec(1, [])



def rec(k: int):
    if (k == M + 1):
        temp = []
        for i in range(1, M+1):
            temp.append(selected[i])
        print(temp)
    else:
        start: int = selected[k-1]
        if start == 0:
            start = 1
        for cand in range(start, N+1):
            # k번째에 cand가 올 수 있으면
            selected[k] = cand
            rec(k + 1)
            selected[k] = 0


N = 4
M = 3
selected = [0] * (N+1)
rec(1)

############################


def rec(k, chosen):
    if len(chosen) >= M:
        print(chosen)
        return

    for i in range(k, N+1):
        chosen.append(i)
        rec(i, chosen)
        chosen.pop()


rec(1, [])

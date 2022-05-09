N = 3
M = 2
selected = [0] * (N+1)
used = [0] * (N+1)


def rec(k: int):
    if (k == M + 1):
        for i in range(1, M+1):
            sb.append(selected[i])
    else:
        for cand in range(1, N+1):
            if (used[cand] == 1):
                continue
            # k번째에 cand가 올 수 있으면
            selected[k] = cand
            used[cand] = 1
            rec(k + 1)
            selected[k] = 0
            used[cand] = 0


M = 3
N = 2
selected = [0] * (N + 1)
rec(1)

########################


def rec(k, chosen):
    if len(chosen) >= M:
        print(chosen)
        return
    for i in range(1, N+1):
        if used[i]:
            continue

        used[i] = 1
        chosen.append(i)
        rec(i, chosen)
        chosen.pop()
        used[i] = 0


N = 3
M = 2
used = [0] * (N+1)
rec(-1, [])

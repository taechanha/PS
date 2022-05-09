def rec(k: int):
    if (k == M + 1):
        for i in range(1, M+1):
            sb.append(selected[i])
    else:
        for cand in range(selected[k-1]+1, N+1):
            # k번째에 cand가 올 수 있으면
            selected[k] = cand
            rec(k + 1)
            selected[k] = 0
M = 3
N = 2
selected = [0] * (N + 1)
rec(1)

#####################                        

def rec(k, chosen):
    if len(chosen) >= M:
        print(chosen)
        return
		
    for i in range(k, N+1):
        if i in chosen:
            continue
        chosen.add(i)
        rec(i, chosen)
        chosen.remove(i)

M=3
N=2
rec(1, set())

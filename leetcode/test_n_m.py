# 순서 상관 X 중복 X

n, m = map(int, input().split())

def rec(k, chosen):
    if len(chosen) >= m:
        print(' '.join(map(str, chosen)))
        return
    
    start = chosen_idx[k-1]
    if start == 0:
        start = 1
    for i in range(start, n+1):
        if i in chosen:
            continue
        chosen_idx[k] = i
        chosen.append(i)
        rec(k+1, chosen)
        chosen_idx[k] = 0
        chosen.pop()

chosen_idx = [0] * (n+1)
rec(1, [])
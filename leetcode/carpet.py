def solution(brown, red):
    nm = brown + red
    for n in range(1, nm+1):
        if nm % n != 0:
            continue
        m = nm//n
        if (n-2)*(m-2) == red:
            return sorted([n, m], reverse=True)


solution(10, 2)

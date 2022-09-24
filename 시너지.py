si = input
N, K, S = map(int, si().split())
a = list(map(int, si().split()))
synergy = list(map(int, si().split()))
min_synergy, max_synergy = min(synergy)-1, max(synergy)-1

ans = 0
cnt = sum(a[:K])

for start in range(N-K):
    end = start + K - 1
    if start <= min_synergy and max_synergy <= end:
        ans = max(ans, 2*cnt)
    else:
        ans = max(ans, cnt)
    
    cnt -= a[start]
    if end+1 < N:
        cnt += a[end+1]

print("answer: ", ans)

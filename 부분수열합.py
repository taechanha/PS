
def solution(N, S, seq):
    global ans, used
    ans = 0
    used = [0] * N

    find(0, 0)

    return ans


def find(i, total):
    global S, seq, ans, used
    if total == S:
        ans += 1
    if i == N:
        return

    for k in range(i, N):
        if used[k]:
            continue
        total += seq[i]
        used[k] = True
        find(i+1, total)
        total -= seq[i]
        used[k] = False


N, S = map(int, input().split())
seq = list(map(int, input().split()))
ans = solution(N, S, seq)
print(ans)

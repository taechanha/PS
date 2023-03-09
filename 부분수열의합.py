# {-7 -3 -2 5 8}

def solution(n, s, arr):
    global cnt, is_used
    cnt = 0
    is_used = [0] * (n+1)
    find(0, 0, [])

    return cnt


def find(i, part_sum, chosen):
    global is_used
    if i == n:
        return
    if part_sum == s and i != 0:
        global cnt
        cnt += 1
        print(chosen, is_used)

    for j in range(n):
        if not is_used[j]:
            val = arr[j]
            is_used[j] = 1
            find(j+1, part_sum+val, chosen+[val])
            is_used[j] = 0


n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = solution(n, s, arr)
print(ans)

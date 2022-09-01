##################### 4:21 ~ 다시 시도~ #################################

# 같다면 백트래킹
# 다르다면 더 작은 것을...

n = int(input())
string = ""
for _ in range(n):
    string += input()


def dfs(left, right, chosen):
    if left > right:
        memo[left][right] = chosen
        return chosen

    if memo[left][right] != -1:
        return chosen

    while string[left] != string[right]:
        if string[left] > string[right]:
            chosen += string[right]
            right -= 1
        else:
            chosen += string[left]
            left += 1

    case1 = dfs(left+1, right, chosen+string[left])
    case2 = dfs(left, right-1, chosen+string[right])
    memo[left][right] = min(case1, case2)
    return memo[left][right]


memo = [[-1] * 2001 for _ in range(2001)]
res = dfs(0, n-1, "")

while len(res) > 80:
    print(res[:80])
    res = res[80:]
print(res)

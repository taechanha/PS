# n개의 수로 이루어진 수열
# 연속된 몇 개의 수를 선택
# 가장 큰 합 구하기
#
# N <= 100,000

# 10, -4, 3, 1, 5, 6, -35, 12, 21, -1
# => 33

def solution(arr):
    if all(x < 0 for x in arr):
        return max(arr)

    total = 0
    max_total = 0
    for i, x in enumerate(arr):
        total += x
        if total < 0:  # 다음 수를 더했을 때 음수가 된다면, 다음 수를 더하는 것이 의미가 없어짐
            total = 0            # 추가로, 연속된 수를 선택하는 것이기 때문에, 여태까지 선택한 연속성은 끊겨야함

        max_total = max(max_total, total)
        # 다음 수를 더했을 때 음수가 되는 것이 아니라면 더하고 넘어감
        # 음수가 된다면 건너뛰고 새로 시작

    return max_total


n = int(input())
arr = list(map(int, input().split()))
ans = solution(arr)
print(ans)

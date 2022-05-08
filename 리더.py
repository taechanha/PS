# dp = {}


# def solution(abilities, k):
#     def helper(i, j, k):
#         if (i, j, k) in dp:
#             return dp[(i, j, k)]

#         if i == j:
#             return abilities[i]

#         if i > j:
#             return 0

#         if k == 0:
#             dp[(i, j, k)] = max(helper(i + 1, j - 1, 0),
#                                 helper(i + 2, j - 1, 0)) + abilities[j]
#             return dp[(i, j, k)]

#         dp[(i, j, k)] = max((helper(i + 2, j - 1, k - 1) + abilities[j]), (helper(i +
#                                                                                   1, j - 2, k - 1) + abilities[j]), (helper(i + 2, j - 2, k) + abilities[j]))
#         return dp[(i, j, k)]

#     n = len(abilities) // 2 * 2  # even number of people.  odd number of people is not allowed.  so we can ignore the last person.  and we can use the same function for both even and odd number of people.  but we need to make sure that the last person is taken by us only when we have used our priority.  so we need to make sure that the total number of rounds played is equal to the quotient of (number of people + 1) divided by 2.

#     return helper(0, n-1, k)


# def solution(abilities, k):
#     dp = {}
#     def helper(abilities, k, i, j):
#         if (i, j, k) in dp:
#             return dp[(i, j, k)]
#         if i == j:
#             return abilities[i]
#         if i > j:
#             return 0
#         if k == 0:
#             return max(abilities[i:j+1])
#         dp[(i, j, k)] = max(helper(abilities, k-1, i+1, j), helper(abilities, k, i+1, j-1)) + abilities[i]
#         return dp[(i, j, k)]
#     return helper(abilities, k, 0, len(abilities)-1)

# memo = {}
# def solution(abilities, k):
#     def helper(abilities, k):
#         if (tuple(abilities), k) in memo:
#             return memo[(tuple(abilities), k)]
#         if len(abilities) == 0:
#             return 0
#         if len(abilities) == 1:
#             return abilities[0]

#         max_sum = 0

#         for i in range(len(abilities)):
#             if i == 0 and k > 0:
#                 max_sum = max(max_sum, abilities[i] + helper([x for x in abilities[1:]], k-1))
#             else:
#                 max_sum = max(max_sum, abilities[i] + helper([x for x in abilities[:i] + abilities[i+1:]], k))

#         memo[(tuple(abilities), k)] = max_sum

#         return max_sum

#     return helper([x for x in sorted(abilities, reverse=True)], k)

# memo = {}


# def solution(abilities, k):
#     def helper(abilities, k, i, j):
#         if (i, j, k) in memo:
#             return memo[(i, j, k)]
#         if i == j:
#             return abilities[i]
#         if i > j:
#             return 0
#         if k == 0:
#             return max(abilities[i:j+1])
#         memo[(i, j, k)] = max(helper(abilities, k-1, i+1, j) +
#                               abilities[i], helper(abilities, k, i+1, j))
#         return memo[(i, j, k)]
#     return helper(abilities, k, 0, len(abilities)-1)


def solution(abilities, k):
    n = len(abilities)
    dp = [[0]*(k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = max(dp[i-1][j], dp[i-2][j-1] + abilities[i-1])

    return dp[n][k]


# abilities = [2, 8, 3, 6, 1, 9, 1, 9]
# k = 2
# 21
abilities = [7, 6, 8, 9, 10]
k = 1
# 22

res = solution(abilities, k)

print(res)


# 당신은 새로 만들어진 두 개의 팀 중 한 팀을 이끄는 리더입니다. 당신은 상대 팀 리더와 경쟁을 통해 사람들을 팀으로 데려옵니다. 매 라운드마다 각 리더는 사람을 한 명씩 선택할 수 있으며, 항상 상대 팀 리더가 먼저 선택합니다. 대신, 당신에게는 원할 때 쓸 수 있는 우선권 k개가 주어집니다. 우선권을 사용한 라운드는 당신이 상대 리더보다 먼저 선택할 수 있습니다.

# 당신을 포함하여 리더는 항상 남은 사람들 중 가장 능력치가 높은 사람을 먼저 데려갑니다. 당신은 이 우선권을 이용해 팀원의 능력치 합이 최대한 높은 팀을 만들려고 합니다.

# 예를 들어 사람들의 능력치를 담은 배열이 [2, 8, 3, 6, 1, 9, 1, 9]이고, 당신에게 우선권이 2개 있는 경우, 다음과 같이 행동할 수 있습니다.

# 첫 번째 라운드에서는 우선권을 사용하지 않습니다. 상대는 능력치가 9인 사람을 데려가고, 당신은 능력치가 9인 사람을 데려갑니다. 남은 사람들의 능력치는 [2, 8, 3, 6, 1, 1]입니다.
# 두 번째 라운드에서는 우선권을 사용합니다. 당신은 능력치가 8인 사람을 데려가고, 상대는 능력치가 6인 사람을 데려갑니다. 남은 사람들의 능력치는 [2, 3, 1, 1]입니다.
# 세 번째 라운드에서도 우선권을 사용합니다. 당신은 능력치가 3인 사람을 데려가고, 상대는 능력치가 2인 사람을 데려갑니다. 남은 사람들의 능력치는 [1, 1]입니다.
# 네 번째 라운드부터는 우선권을 모두 소진했기 때문에 나중에 선택할 수밖에 없습니다. 당신과 상대는 각각 능력치가 1인 사람을 데려갑니다.
# 위와 같이 행동할 경우 당신은 능력치 합이 9+8+3+1=21인 팀을 만들 수 있습니다. 다른 방법으로 팀원을 선택할 수도 있지만, 능력치 합이 21보다 큰 팀은 만들 수 없습니다.

# 만약 사람들의 수가 홀수인 경우, 마지막에 남은 한 사람은 우선권을 사용한 경우에만 당신이 데려갈 수 있습니다. 즉, 진행되는 라운드의 총횟수는 (사람 수 + 1)를 2로 나눈 몫과 같습니다.

# 사람들의 능력치를 담은 정수 배열 abilities와 우선권의 개수를 나타내는 정수 k가 매개변수로 주어집니다. 우선권을 k번 이하로 사용하여 만들 수 있는 팀의 능력치 합의 최댓값을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ abilities의 길이 ≤ 300,000
# 1 ≤ abilities의 원소 ≤ 109
# 0 ≤ 2 * k ≤ abilities의 길이 + 1
# 입출력 예
# abilities	k	result
# [2, 8, 3, 6, 1, 9, 1, 9]	2	21
# [7, 6, 8, 9, 10]	1	22
# 입출력 예 설명
# 입출력 예 #1

# 문제 예시와 같습니다.

# 입출력 예 #2

# 다음과 같이 행동하면 됩니다.

# 첫 번째 라운드에서는 우선권을 사용하지 않습니다. 상대 리더는 능력치 10인 사람을, 당신은 능력치 9인 사람을 데려갑니다.
# 두 번째 라운드에서도 우선권을 사용하지 않습니다. 상대 리더는 능력치 8인 사람을, 당신은 능력치 7인 사람을 데려갑니다.
# 세 번째 라운드에서 우선권을 사용합니다. 당신은 능력치 6인 사람을 데려갑니다.
# 그 결과, 당신은 능력치 합이 9+7+6=22인 팀을 만들 수 있습니다. 다른 방법으로 팀원을 선택할 수도 있지만, 능력치 합이 22보다 큰 팀은 만들 수 없습니다. 따라서 22를 return 합니다.

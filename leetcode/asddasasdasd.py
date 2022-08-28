from collections import defaultdict


def solution(balance, transaction, abnormal):
    answer = []

    data = defaultdict(list)

    # init data
    for i in range(len(balance)):
        data[i+1].append((i+1, balance[i]))

    print("init: ", data)

    # handle transaction
    for i, (from_, to_, target) in enumerate(transaction):
        # from 처리
        process(from_, to_, target, data)
        # to 처리
        # data[to_].append((from_, target))

        print(from_, to_, target, data)

    print("after transaction: ", data)

    # handle abnormal
    ans = defaultdict(int)
    # init ans
    for i in range(len(balance)):
        ans[i+1] = 0

    print("asadsasd ", ans)

    abnormal = set(abnormal)
    for k in data.keys():
        for user, amt in data[k]:
            if user in abnormal:
                continue
            ans[k] += amt

    print("ans: ", ans)

    answer = []
    for k, v in ans.items():
        answer.append(v)

    return answer


def process(from_, to_, target, data):

    while True:

        user, amt = data[from_].pop()
        if amt > target:
            data[from_].append((user, amt-target))
            data[to_].append((user, target))
            break
        elif amt == target:
            data[to_].append((user, amt))
            break

        target -= amt
        data[to_].append((user, amt))


balance = [30, 30, 30, 30]
transaction = [[1, 2, 10], [2, 3, 20], [3, 4, 5], [3, 4, 30]]
abnormal = [2, 3]
res = solution(balance, transaction, abnormal)
print(res)

# 1. 가장 최근 받은 재화부터 pop
# 2. 유저마다의 재화를 추적해야

# {
#     user_index: [(user_index, amt)]
# }

# [30, 30, 30, 30]

# [[1, 2, 10]
# [2, 3, 20]
# [3, 4, 5]
# [3, 4, 30]

# [1]

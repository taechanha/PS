from itertools import permutations as pm


def compare(u: str, b: str):
    # 길이가 다르면 false
    if len(u) != len(b):
        return False
    # 같으면 문자 일대일 대응해서, 같은 문자거나 b가 *인 경우 패스, 아니면 false
    for i in range(len(u)):
        if b[i] == '*':
            continue
        if u[i] != b[i]:
            return False
    return True


def solution(user_id, banned_id):
    banned_id = list(set(banned_id))
    n, m = len(user_id), len(banned_id)
    ans = 0
    # base
    user_ids = list(set(pm(user_id)))
    banned_ids = list(set(pm(banned_id)))
    set_list = set()
    for banned_id in banned_ids:
        i = 0
        while i < n:
            new_list = []
            temp_i = i
            j = 0
            while j < m:
                if compare(user_id[temp_i], banned_id[j]):
                    new_list.append(user_id[temp_i])
                    new_list.append(banned_id[j])
                    temp_i += 1
                    j += 1
                else:
                    temp_i += 1
                if temp_i >= n-1:
                    break
            # matched
            if j >= m:
                ans += 1
                set_list.add(tuple(new_list))
            i += 1

    for each in set_list:
        print(each)
    # print(len(set_list))
    return len(set_list)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
res = solution(user_id, banned_id)
print(res)

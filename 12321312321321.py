from bisect import bisect_left, bisect_right


def is_included(n: str, registered_list):
    if n not in registered_list:
        return False

    return True


def split(s):
    ns = ""
    nn = ""
    for ch in s:
        if ch.isalpha():
            ns += ch
        else:
            nn += ch
    return ns, nn


def solution(registered_list, new_id):

    if new_id not in registered_list:
        return new_id

    s, n = split(new_id)

    n_list = []
    for each in registered_list:
        es, en = split(each)
        if es == s:
            if en == "":
                continue
            n_list.append(int(en))

    registered_list = n_list
    registered_list.sort()

    # print(registered_list)
    found = 0
    for i in range(0, len(registered_list)-1):
        # print(i, registered_list[i+1], registered_list[i])
        if registered_list[i+1] != registered_list[i]+1:
            found = 1
            break

    if found:
        return s + str(registered_list[i]+1)
    else:
        return s + str(registered_list[-1]+1)

    n = new_id
    while is_included(new_id, registered_list):
        s, n = split(new_id)
        n = 0 if n == "" else n
        n = str(int(n)+1)
        new_id = s + n

    return new_id


registered_list = ["card", "ace13", "ace16", "banker", "ace17", "ace14"]
# registered_list = ["ace13", "ace16", "ace15", "ace17", "ace14"]
registered_list = ["apple1", "orange", "banana3"]
# new_id = "ace15"
new_id = "apple"

registered_list = ["bird99", "bird98", "bird101", "gotoxy"]
new_id = "bird98"
registered_list = ["cow", "cow1", "cow2", "cow3",
                   "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"]
new_id = "cow"
res = solution(registered_list, new_id)
print(res)

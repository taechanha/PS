# skill	skill_trees	return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2


def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        if check(skill, skill_tree):
            cnt += 1

    return cnt


def check(skill, skill_tree):
    if skill == '' or skill_tree == '':
        return 1
    if skill_tree[0] in skill:
        if skill_tree[0] != skill[0]:
            return 0
        else:
            return check(skill[1:], skill_tree[1:])
    else:
        return check(skill, skill_tree[1:])


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

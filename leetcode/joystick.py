def ctrl_char(chr):
    return min(ord(chr) - ord('A'), ord('Z') - ord(chr) + 1)


def count_str(name):
    count = 0
    for idx in range(len(name)):
        x = name[idx]
        count += ctrl_char(x)
        if name[idx+1:] == 'A' * (len(name) - idx - 1):
            return count
        if idx == len(name) - 1:
            return count
        count += 1
    return count


def solution(name):
    name_l = name
    name_r = name[0] + name[::-1][:-1]
    count_l = count_str(name_l)
    count_r = count_str(name_r)
    return min(count_l, count_r)


solution("JAAAZA")

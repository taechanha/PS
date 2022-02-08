import string


def contain_aeiou(s: str):
    for each in s:
        if each in vowel:
            return True
    return False


def is_conso_or_vow_consecutive_3_times(s: str):
    if len(s) < 3:
        return False

    def is_all_conso(s: str):
        for each in s:
            if each not in conso:
                break
        else:
            return True
        return False

    def is_all_vowel(s: str):
        for each in s:
            if each not in vowel:
                break
        else:
            return True
        return False

    for i in range(len(s) - 2):
        concat_s = s[i] + s[i+1] + s[i+2]
        if is_all_conso(concat_s) or is_all_vowel(concat_s):
            return True
    return False


def is_ch_consecutive(s: str):
    if len(s) < 2:
        return False

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            if s[i] != 'e' and s[i] != 'o':
                return True
    return False


si = input()
alpha_list = string.ascii_lowercase
vowel = set(['a', 'e', 'i', 'o', 'u'])
conso = set(alpha_list) - vowel

while si != 'end':

    if (not contain_aeiou(si)) \
            or is_conso_or_vow_consecutive_3_times(si)\
            or is_ch_consecutive(si):
        print(f'<{si}> is not acceptable.')

    else:
        print(f'<{si}> is acceptable.')

    si = input()

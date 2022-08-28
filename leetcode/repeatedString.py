def repeatedString(s, n):
    cnt = 0
    for char in s[:n]:
        if char == 'a':
            cnt += 1
    if cnt == 0:
        return 0

    q, r = divmod(n, len(s))
    cnt_r = 0
    for char in s[:r]:
        if char == 'a':
            cnt_r += 1
    return cnt * q + cnt_r


print(repeatedString('gfcaaaecbg', 547602))

def reverse_each(s):
    temp = ""
    for each in s.split():
        temp += each[::-1] + " "
    return temp[:-1]


s = input()
i = 0
ans = ""

while i < len(s):
    ch = s[i]
    temp_s = s[i:] # to move forward, s fixed
    if ch == '<':
        # find >'s idx
        end_idx = temp_s.index('>') + 1
        ans += temp_s[:end_idx]
        # move forward
        i += end_idx
    else:
        # <가 temp_s에 있으면, < 위치를 찾아서 >전 까지를 reverse order로 출력(space 구분해서)
        if '<' in temp_s:
            start_idx = temp_s.index('<')

            ans += reverse_each(temp_s[:start_idx])  # temp_s[:start_idx][::-1]
            end_idx = temp_s.index('>') + 1
            ans += temp_s[start_idx:end_idx]
            i += end_idx
        else:
            # 없으면? HI HAHA -> AHAH IH 처럼 출력
            ans += reverse_each(temp_s)
            i = len(s)
print(ans)

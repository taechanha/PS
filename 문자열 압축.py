def solution(s):
    n = len(s)
    len_shortest_string = len(s)
    # curr_chunk = s[i:i+step]
    # next_chunk = s[i+step:i+step*2]
    # if len(next_chunk) < step:
    #     break
    # if curr_chunk == next_chunk:
    for step in range(3, n//2+1):
        temp = ""
        cnt = 1
        to_copy = ""
        fl = 0
        i = 0
        while i < n-1:
            s1 = str(s[i:i+step])
            s2 = str(s[i+step:i+step*2])
            if len(s1) != len(s2):
                temp += s1 + s2
                break
            if is_same(s1, s2):
                to_copy = s1
                cnt += 1
                i = i+step*2
                continue
            else:
                if to_copy == "":
                    temp += s[i]
                    i += 1
                    continue
                if cnt == 1:
                    temp += to_copy
                else:
                    temp += str(cnt) + to_copy  # 2a2b
                    if i+step*2 >= n-1:
                        fl = 1
                        break
                to_copy = ""
                cnt = 1
            i += 1

        # if fl == 0:
        #     if cnt == 1:
        #         temp += to_copy  # no duple left
        #     else:
        #         temp += str(cnt) + to_copy  # like ccc left

        print(temp)

        # print(step, curr_chunk, next_chunk, i)
        print("\n-----------\n")
    return


def is_same(s1, s2):
    return s1 == s2
    pass

# "aabbaccc" -> "2a2ba3c"
# "ababcdcdababcdcd" -> "2ab2cd2ab2cd" (2) -> "2ababcdcd" (8)

# (step: 1) s[0:1] s[1:2] s[2:3] ... s[n-2:n-1]. done
#      a      a       b    ...

# (step: 2) s[0:2] s[1:3] s[2:4] s[6:8]
#      aa     bb      ac     cc

# generalize:
#   curr_chunk == next_chunk?
#   curr_chunk: s[i:i+step]

# step: range(1, len(s)//2+1)


# s = "aabbaccc"
#s = "ababcdcdababcdcd"
s = "abcabcdede"
res = solution(s)

print(res)


# curr_chunk = s[i:i+step]
# next_chunk = s[i+step:i+step*2]
# if len(next_chunk) < step:
#     break
# if curr_chunk == next_chunk:

# aaabbccd    [ aaa bb cc ]

# ababcdcdababcdcd

# (1) -> same

# (2) -> 2ab2cd2ab2cd    [ abab cdcd abab cdcd ]

# (8) -> 2ababcdcd       [ ababcdcd ababcdcd ]

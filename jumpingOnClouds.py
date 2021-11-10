def jumpingOnClouds(c):
    cnt = 0
    i = 0
    c += [1]

    while i < len(c) - 2:
        if c[i+2] == 1:
            i += 1
            cnt += 1
        else:
            i += 2
            cnt += 1

    return cnt


a = """
0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0
"""
test = [int(i) for i in a if i.isdigit()]

print(jumpingOnClouds(test))

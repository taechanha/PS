# sequence subsequence
# person compression
# VERDI vivaVittorioEmanueleReDiItalia
# caseDoesMatter CaseDoesMatter

def is_substring(s, t):
    i = 0
    for each in t:
        if each == s[i]:
            i += 1
            if i == len(s):
                return True
    else:
        return False


si = input().split()

while si:
    s, t = si[0], si[1]
    if is_substring(s, t):
        print("Yes")
    else:
        print("No")

    try:
        si = input().split()
    except:
        exit()

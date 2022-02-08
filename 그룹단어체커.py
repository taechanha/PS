
def appear_again(index, ch):
    for i in range(index + 1, len(s)):
        if s[i] == ch:
            return True
    return False


t = int(input())
count = t
while t:
    t -= 1

    s = input()

    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            if appear_again(i+1, s[i]):
                count -= 1
                break

print(count)

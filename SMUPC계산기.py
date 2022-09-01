# 8:10 ~


mapping = {
    'S': lambda x, y: x-y,
    'M': lambda x, y: x*y,
    'U': lambda x, y: x//y if x > 0 else - (abs(x)//y),
    'P': lambda x, y: x+y,
}


def validate(si):
    keyword = set(['S', 'M', 'U', 'P', 'C'])
    if not (si[0].isdigit() and si[-1].isalpha()):
        # print(1)
        return False
    if '-' in si:
        # print(2)
        return False
    for ch in si:
        if not (ch in keyword or (0 <= int(ch) <= 9)):
            # print(3)
            return False
    for i in range(len(si)-1):
        if si[i] in keyword-{'C'} and si[i+1] in keyword-{'C'}:
            # print(4)
            return False
    return True


n = int(input())
si = input()
answer = []

# validate
# if not validate(si):
# print("NO OUTPUT")

# process; number
data = []
num = ""
for ch in si:
    if ch.isalpha():
        if num:
            data.append(num)
            num = ""
        data.append(ch)
    elif ch.isdigit():
        num += ch


left = op = right = None
for atom in data:
    if atom.isdigit():
        if left == None:
            left = int(atom)
        else:
            right = int(atom)
    elif atom.isalpha():
        if atom == 'C':
            answer.append(left)
            continue
        op = atom

    if left and op and right:
        left = mapping[op](left, right)
        right = None
        op = None

print(*answer) if answer else print("NO OUTPUT")

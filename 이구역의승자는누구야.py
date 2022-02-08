alpha2num = {
    'a': 3,
    'b': 2,
    'c': 1,
    'd': 2,
    'e': 3,
    'f': 3,
    'g': 3,
    'h': 3,
    'i': 1,
    'j': 1,
    'k': 3,
    'l': 1,
    'm': 3,
    'n': 3,
    'o': 1,
    'p': 2,
    'q': 2,
    'r': 2,
    's': 1,
    't': 2,
    'u': 1,
    'v': 1,
    'w': 2,
    'x': 2,
    'y': 2,
    'z': 1
}


alpha_str = input().lower()
arr = []

for i in range(len(alpha_str)):
    arr.append(alpha2num[alpha_str[i]])

cnt = 3
while len(arr) > 1:
    temp_arr = []

    for i in range(1, len(arr), 2):
        temp_arr.append(arr[i-1] + arr[i])

    # special case
    if len(arr) % 2 != 0:
        temp_arr.append(arr[-1])

    arr = temp_arr


if arr[0] % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")

# 01234 012 01
# ABCDE BDE DE

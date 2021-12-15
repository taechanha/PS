def is_vowel(char):
    if keyboard[char][0] >= 5 or (keyboard[char][0] == 4 and keyboard[char][1] == 0):
        return True
    return False


keyboard = {}
x = 0
y = 2

for char in 'qwertyuiopasdfghjklzxcvbnm':
    if char == 'a':
        x, y = 0, 1
    if char == 'z':
        x, y = 0, 0

    keyboard[char] = [x, y]
    x += 1

left, right = map(str, input().split())
string = list(map(str, input().split()))[0]
time = 0

for char in string:
    if is_vowel(char):
        dist = abs(keyboard[right][0] - keyboard[char][0]) + \
            abs(keyboard[right][1] - keyboard[char][1])
        right = char
    else:
        dist = abs(keyboard[left][0] - keyboard[char][0]) + \
            abs(keyboard[left][1] - keyboard[char][1])
        left = char

    time += dist + 1

print(time)

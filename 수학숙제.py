# 6:23 ~ 6:28

# 조건
# 002 -> 2
# 가능한 가장 큰 숫자: jj4123b -> 4123
# 출력: 오름차순

def get_num(string):
    data = []
    new = ""
    for ch in string:
        if ch.isdigit():
            new += ch
        else:
            if not new:
                continue
            data.append(new)
            new = ""
    if new:
        data.append(new)
    return data


n = int(input())
answer = []
for i in range(n):
    string = input()
    data = get_num(string)
    for num in data:
        answer.append(int(num))

answer.sort()

for row in answer:
    print(row)


# 6:03 ~ 6:35

def preprocess(data: str) -> list:
    skip = False
    temp = []
    for i in range(len(data)-1):
        if skip:
            skip = False
            continue
        if data[i] == '[':
            tup = (data[i], data[i+1])
            temp.append(tup)
            skip = True
        else:
            temp.append(data[i])
    return temp


def split_(temp: list):
    var = ""
    keyword = []
    for ch in temp:
        if type(ch) == tuple:
            keyword.append(ch)
        elif ch in ('*', '[', ']', '&'):
            keyword.append(ch)
        elif 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            var += ch
    return keyword, var


def reverse(keyword: str) -> str:
    temp = ""
    for ch in keyword[::-1]:
        if type(ch) == tuple:
            temp += ch[0] + ch[1]
        else:
            temp += ch
    return temp


si = input().split()

output_stream = []
for data in si[1:]:

    # preprocess
    temp = preprocess(data)
    # split temp to keyword and variable
    keyword, var = split_(temp)
    # reverse string
    keyword = reverse(keyword)

    # answer
    answer = si[0] + keyword + " " + var + ";"
    output_stream.append(answer)

for row in output_stream:
    print(row)

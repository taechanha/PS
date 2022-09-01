# 5:58 ~

idx = int(input())-1
n = fixn = int(input())
data = [1, 2, 3, 4, 5]

cnt = 0
c = 1
i = 0
tmp = []
while n > 0:
    if data[i] == fixn:
        n -= 1
    tmp.append(data[i])
    if 0 <= i < 4:
        i += c
    else:
        c = -c
        i += c

    cnt += 1
print(tmp)
print(cnt)

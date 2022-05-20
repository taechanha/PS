k = int(input())
s = []
while k:
    k -= 1
    si = int(input())

    if si != 0:
        s.append(si)
    else:
        s.pop()

print(sum(s))

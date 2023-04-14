def d(n):
    s = 0
    for x in str(n):
        s += int(x)
    return n + s

size = 10_001
outs = []
record = set(range(1, size))
for i in range(1, size):
    point = d(i)
    if point in record:
        record.remove(point)
        
[print(x) for x in record]
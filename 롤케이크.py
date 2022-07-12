# 6:45 ~

n, cuts = map(int, input().split())
cakes = list(map(int, input().split()))
cakes1 = []
cakes2 = []

for cake in cakes:
    if cake % 10 == 0:
        cakes1.append(cake)
    else:
        cakes2.append(cake)

cakes1.sort()
cakes2.sort()

pieces = 0

for cake in cakes1:
    if cake == 10:
        pieces += 1
        continue
    q = cake // 10
    if cuts >= q-1:
        pieces += q
        cuts -= q-1
    else:
        while cake > 10 and cuts > 0:
            cake -= 10
            cuts -= 1
            pieces += 1
        if cake == 10:
            pieces += 1
            continue

for cake in cakes2:
    # cut cake
    while cake > 10 and cuts > 0:
        cake -= 10
        cuts -= 1
        pieces += 1
    if cake == 10:
        pieces += 1
        continue

print(pieces)

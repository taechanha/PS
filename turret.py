from math import sqrt
T = int(input())
while T:
    T -= 1

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt((x1-x2)**2 + (y1-y2)**2)

    if r1 > r2:
        r2, r1 = r1, r2

    # 두 점에서 만남
    if r2 - r1 < d and d < r1 + r2:
        print(2)
    # 한 점에서 만남(외접/내접)
    elif (r1 + r2 == d or r2 - r1 == d) and d != 0:
        print(1)
    # 만나지 않음
    elif r1 + r2 < d or d < r2 - r1:
        print(0)
    # 두 원이 같음
    else:
        if r1 == r2:
            print(-1)
        else:
            print(0)

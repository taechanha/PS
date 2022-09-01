# 5:18 ~ 6: 00

# 세그먼트 트리 -> 복기


from collections import defaultdict

n = int(input())
box = defaultdict(int)

for _ in range(n):
    si = list(map(int, input().split()))
    si_n = len(si)
    if si_n == 2: # out
        # 사탕 빼기, rank인 요소를 amt 개수 만큼
        out_, rank, amt = si
        if box[rank] > amt:
            pass
        elif box[rank] == amt:
            pass
        else:
            pass
    else: # in
        in_, rank, amt = si
        # 사탕 빼기, rank인 요소를 amt 개수 만큼
        if amt < 0:
            if box[rank] > amt:
                pass
            elif box[rank] == amt:
                pass
            else:
                pass
        # 사탕 넣기, amt 개수 만큼
        box[rank] += amt
        
    
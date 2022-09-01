

def flat_bowl(fish_bowl, temp):
    idx = 0
    for j in range(len(temp[0])):
        for i in range(len(temp)-1, -1, -1):
            fish_bowl[idx] = temp[i][j]
            idx+=1

def rotate(temp, n, m):
    ret = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ret[j][n-1-i] = temp[i][j]
    return ret

def adjust_fish(fish_bowl, temp, s):
    n, m = len(temp), len(temp[0])
    temp[-1].extend(fish_bowl[s:])
    move_fishes = [[0]*len(temp[i]) for i in range(n)]

    for r in range(len(temp)):
        for c in range(len(temp[r])):
            for d in [1,2]:
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < n and 0 <= nc < len(temp[nr]):
                    diff = abs(temp[r][c] - temp[nr][nc])//5
                    if temp[r][c] < temp[nr][nc]: diff*=-1
                    move_fishes[r][c] -= diff
                    move_fishes[nr][nc] += diff

    for i,j in [(i,j) for i in range(n) for j in range(m)]:
        temp[i][j] += move_fishes[i][j]
    
    for i in range(len(move_fishes[0]), len(move_fishes[-1])):
        fish_bowl[i-len(move_fishes[0])+s] += move_fishes[-1][i]

def stack(fish_bowl,s,temp):
    n = len(temp)
    if n > len(fish_bowl) - s: 
        adjust_fish(fish_bowl, temp, s)
        flat_bowl(fish_bowl, temp)
        return

    rotate_bowl = rotate(temp, len(temp), len(temp[0]))
    rotate_bowl.append(list(fish_bowl[s:s+n]))
    s+=n
    stack(fish_bowl, s, rotate_bowl)
    
def fold(fish_bowl):
    temp = [list(fish_bowl[:len(fish_bowl)//2])]
    for _ in range(2):
        temp = rotate(temp, len(temp), len(temp[0]))
    temp.append(fish_bowl[len(fish_bowl)//2:])

    temp2 = []
    temp3 = []
    for bowl in temp:
        temp2.append(bowl[:len(bowl)//2])
        temp3.append(bowl[len(bowl)//2:])

    for _ in range(2):
        temp2 = rotate(temp2, len(temp2), len(temp2[0]))
    for li in (temp3):
        temp2.append(li)
    adjust_fish(fish_bowl, temp2, len(fish_bowl))
    flat_bowl(fish_bowl, temp2) 

def add_fish(fish_bowl):
    min_num = min(fish_bowl)
    for i in range(len(fish_bowl)):
        if min_num == fish_bowl[i]: 
            fish_bowl[i] += 1

def end_cond(fish_bowl, k):
    return max(fish_bowl) - min(fish_bowl) > k

n, k = map(int,input().split())
fish_bowl = list(map(int, input().split()))
dr = [-1,0,1,0]
dc = [0,1,0,-1]

cnt = 0
while end_cond(fish_bowl, k):
    cnt+=1
    add_fish(fish_bowl)
    stack(fish_bowl, 1,[[fish_bowl[0]]])
    fold(fish_bowl)
print(cnt)
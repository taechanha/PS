
def is_end(bowl, k) -> bool:
    return max(bowl) - min(bowl) <= k

def solve(bowl, k) -> int:
    
    while not is_end(bowl, k):
        arrange_cnt += 1
        bowl = arrange_bowl()
    
    return arrange_cnt

def adjust_fishes(board) -> list[list[int]]:
    temp_board = [row[:] for row in board] # deepcopy
    for x in range(n):
        for y in range(n):
            if board[x][y] == -1:
                continue
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if not(0 < nx < n and 0 < ny < n):
                    continue
                if board[nx][ny] == -1:
                    continue
                
                diff = abs(board[nx][ny] - board[x][y])
                d = diff // 5
                if d <= 0:
                    continue
                if board[nx][ny] > board[x][y]:
                    temp_board[nx][ny] -= diff
                    temp_board[x][y] += diff
    return temp_board

def up():
    start_x = 0
    w = 1
    h = 1

    board[w][h] = board[start_x][0]
    board[start_x][0] = -1
    
    # pivot = w = h = 1
    # idx = 0
    # while True:
    #     idx += 1
    #     if pivot - 1 + w + h > n:
    #         break
        
    #     for c in range(pivot, pivot + w):
    #         for r in range(n, n-h, -1): 
    #             next_r = (n - w) + (c - pivot)
    #             next_c = (pivot + w) + (n - r)
    #             board[next_r][next_c] = board[r][c]
    #             board[r][c] = -1
    #     pivot += (idx // 2 + 1)
    #     if idx % 2 == 0:
    #         w += 1
    #     else:
    #         h += 1

# 0 0 0 0 0 0 0
# a b c d e f 0
# 0 1 2 3 4 5 6


def down() -> list[int]:
    bowl = []
    for c in range(0, len(board[0])):
        for r in range(len(board)-1, -1, -1):
            if board[r][c] == -1:
                continue
            bowl.append(board[r][c])
    return bowl

# -1 -1 a b -1 -1 -1 -1
# -1 -1 c d -1 -1 -1 -1
# -1 -1 e f g h -1 -1


def fold():


    pass

def arrange_bowl(bowl) -> list[int]:
    """ 어항 정리 """
    # 1. 물고기의 수가 가장 적은 어항에 물고기 한 마리 추가
    min_fishes = min(bowl)
    for i, fishes in enumerate(bowl):
        if fishes == min_fishes:
            bowl[i] += 1
    

    # 2. 어항 쌓기
    board = up()
    # 3. 어항 속 물고기 수 조절
    board = adjust_fishes(board)

    # 4. 어항을 일렬로 내려 놓기
    bowl = down()
    # 3. 반복
    board = adjust_fishes(board)

    fold()

    pass


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n = 8
k = 7
bowl = [5, 3, 3, 14, 9, 2, 11, 8]
board = [[-1] * 100 for _ in range(100)]
arrange_cnt = 0


### ---- ###
N, K = map(int, input().split())
fish = list(map(int, input().split()))
# N, K = 4, 0
# fish = [1, 10000, 1, 10000]

def fish_shuffle(fish, N):
    # 작은 것에 1씩 더한다
    a = min(fish)
    temp = []
    for i, v in enumerate(fish):
        if v == a:
            temp.append(i)
    for i in temp:
        fish[i] += 1

    # 맨 앞 어항을 2층으로 보낸다
    a = fish.pop(0)
    fish = [fish]
    fish.append([a])

    # 어항 쌓기
    while True:
        floor2 = len(fish[1])
        new_fish = [fish[0][floor2:]]  # 1층 완료
        if len(new_fish[0]) < len(fish): # 층수보다 1층에 남아있는 어항개수가 작으면 stop
            break
        for i in range(floor2):
            b = [fish[j][floor2-i-1] for j in range(len(fish))]
            new_fish.append(b)
        fish = new_fish

    # 어항 속 물고기수 조절하기, 각 어항에서 2방향만 확인
    temp = [[] for i in range(len(fish))]
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            temp[i].append(0)
    for i in range(len(fish)):
        for j, v in enumerate(fish[i]):
            #오른쪽 확인
            try:
                if fish[i][j] > fish[i][j+1]:
                    d = (fish[i][j] - fish[i][j + 1]) // 5
                    temp[i][j] -= d
                    temp[i][j+1] += d
                else:
                    d = (fish[i][j+1] - fish[i][j]) // 5
                    temp[i][j] += d
                    temp[i][j + 1] -= d
            except:
                pass

            #위쪽 확인
            try:
                if fish[i][j] > fish[i+1][j]:
                    d = (fish[i][j] - fish[i+1][j]) // 5
                    temp[i][j] -= d
                    temp[i+1][j] += d
                else:
                    d = (fish[i+1][j] - fish[i][j]) // 5
                    temp[i][j] += d
                    temp[i+1][j] -= d
            except:
                pass


    for i in range(len(fish)):
        for j in range(len(fish[i])):
            fish[i][j] += temp[i][j]

    # 일렬 배치
    new_fish = []
    for j in range(len(fish[1])):
        new_fish.append(len(fish))
    for i in range(len(fish[0])-len(fish[1])):
        new_fish.append(1)

    temp = []
    for i in range(len(new_fish)):
        for j in range(new_fish[i]):
            temp.append(fish[j][i])
    fish = temp


    # 1번 접기
    floor1 = fish[N//2:]
    new_fish = [floor1]
    temp = []

    for i in range(N//2):
        temp.append(fish[N//2-i-1])
    new_fish.append(temp)
    fish = new_fish

    # 2번 접기
    new_fish = [fish[0][N//4:], fish[1][N//4:], list(reversed(fish[1][:N//4])), list(reversed(fish[0][:N//4]))]
    fish = new_fish
    # 다시 물고기 조절 작업
    # 어항 속 물고기수 조절하기, 각 어항에서 2방향만 확인

    temp = [[] for i in range(len(fish))]
    for i in range(len(fish)):
        for j in range(len(fish[i])):
            temp[i].append(0)

    for i in range(len(fish)):
        for j, v in enumerate(fish[i]):
            #오른쪽 확인
            try:
                if fish[i][j] > fish[i][j+1]:
                    d = (fish[i][j] - fish[i][j + 1]) // 5
                    temp[i][j] -= d
                    temp[i][j+1] += d
                else:
                    d = (fish[i][j+1] - fish[i][j]) // 5
                    temp[i][j] += d
                    temp[i][j + 1] -= d
            except:
                pass

            #위쪽 확인
            try:
                if fish[i][j] > fish[i+1][j]:
                    d = (fish[i][j] - fish[i+1][j]) // 5
                    temp[i][j] -= d
                    temp[i+1][j] += d
                else:
                    d = (fish[i+1][j] - fish[i][j]) // 5
                    temp[i][j] += d
                    temp[i+1][j] -= d
            except:
                pass

    for i in range(len(fish)):
        for j in range(len(fish[i])):
            fish[i][j] += temp[i][j]

    # 다시 펼치기
    new_fish = []
    for j in range(len(fish[1])):
        new_fish.append(len(fish))
    for i in range(len(fish[0])-len(fish[1])):
        new_fish.append(1)

    temp = []
    for i in range(len(new_fish)):
        for j in range(new_fish[i]):
            temp.append(fish[j][i])
    fish = temp

    # 가장 많이 들어있는 어항, 가장 적게 들어 있는 어항의 물고기 수 차이
    a = min(fish)
    b = max(fish)
    k = max(fish)-min(fish)
    return k, fish

# 메인 함수
count = 1
while True:
    a, fish = fish_shuffle(fish, N)
    if a<=K:
        break
    else:
        count+=1
print(count)




# 0 0 0 0 0 0 0 0
# 5 3 3 6 9 2 7 8

# 0 1 2 3 4 5 6 7 

# ----------------

# 0 0 0 0 0 0 0 0 
# 0 5 0 0 0 0 0 0
# ! 3 3 6 9 2 7 8

# 0 1 2 3 4 5 6 7

# ----------------

# 0 0 0 0 0 0 0 0  
# 0 ! 3 5 0 0 0 0  # rotate: 3 3
# ! ! 3 6 9 2 7 8            6 5

# 0 1 2 3 4 5 6 7
#     s
# ----------------

# 0 0 0 0 3 3 0 0 
# 0 ! ! ! 6 5 0 0
# ! ! ! ! 9 2 7 8

# 0 1 2 3 4 5 6 7

# 0 1 2 3 4 5 6 7

# ! ! 3 6 9 2 7 8   
# 0 ! 3 5 0 0 0 0  rotate: 3 3  -> 5 3  -> 6 5
# 0 0 0 0 0 0 0 0          5 6     6 3     3 3

def rotate903(h, w, base):    
    for i in range(3):
        for r in range(h):
            for c in range(base, base+w):
                board[c][h-r-1] = board[r][c]
    return board




n = len(board); m = len(board[0])
for r in range(n):
    for c in range(m):
        board[n-1-(h-1)-r][base+w-1+c] = mat[n-1-r][base+c]


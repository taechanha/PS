# 학생의 자리 정하기

# 조건
# 1. 비어있는 칸 중, 인접한 칸에 좋아하는 학생이 가장 많은 칸
# 2. 여러 개면, 인접한 칸 중 빈 칸이 가장 많은 칸
# 3. 여러 개면, 행의 번호가 가장 작은 칸, 그것도 여러 개면 열의 번호가 가장 작은 칸

# 답: 각 학생의 만족도의 합
#   - 만족도: 각 학생의 인접한 칸에 앉은 좋아하는 학생의 수


# 인접한 칸 조사 -> 좋아하는 학생 가장 많은 칸 (i, j) 리스트 반환
# 학생 1명에 대한 (i, j) candidate 리스트

def out_of_bound(r, c):
    return not (0 <= r < n and 0 <= c < n)


def cond1(students):
    students_liked = students[1:]
    pos_cnt = []  # [i, j, cnt]
    for r in range(n):
        for c in range(n):
            # 이미 채워져있는 칸은 조사 안 함
            if board[r][c] != 0:
                continue
            cnt = 0
            coord_list = check_surround(r, c)
            for nr, nc in coord_list:
                if board[nr][nc] in students_liked:
                    cnt += 1

            pos_cnt.append([r, c, cnt])

    return filter_list(pos_cnt)


def filter_list(pos_cnt):
    ret = []
    max_cnt = max(pos_cnt, key=lambda x: x[2])[2]
    for each in pos_cnt:
        if each[2] == max_cnt:
            ret.append((each[0], each[1]))
    return ret


def cond2(candidate_list):
    # input: [(i, j, cnt), (k, l, cnt)]
    pos_cnt = []  # [i, j, cnt]
    for r, c in candidate_list:
        cnt = 0
        coord_list = check_surround(r, c)
        for nr, nc in coord_list:
            if board[nr][nc] == 0:  # empty cell
                cnt += 1
        pos_cnt.append([r, c, cnt])

    return filter_list(pos_cnt)


def cond3(candidate_list):
    # input: [(1, 2), (2, 0), ...]
    return sorted(candidate_list, key=lambda x: (x[0], x[1]))[0]


def check_surround(r, c):
    ret = []
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if out_of_bound(nr, nc):
            continue
        ret.append((nr, nc))
    return ret


def level_of_satisfaction(board):
    # make use of stu2like
    satisfaction = 0
    for r in range(n):
        for c in range(n):
            target_student = board[r][c]
            students_liked = stu2like[target_student]
            cnt = 0
            coord_list = check_surround(r, c)
            for nr, nc in coord_list:
                if board[nr][nc] in students_liked:
                    cnt += 1

            satisfaction += calcul_satisfaction(cnt)

    return satisfaction

def calcul_satisfaction(cnt):
    # 0: 0, 1: 1, 2: 10, 3: 100, 4: 1000
    if cnt == 0:
        return cnt
    return 10 ** (cnt - 1)

global n, board, stu2like
n = int(input())
board = [[0] * n for _ in range(n)]
stu2like = dict()
student_list = []
for _ in range(n**2):
    students = list(map(int, input().split()))
    student_list.append(students)

    stu2like[students[0]] = students[1:]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for students in student_list:
    candidate_list = cond1(students)
    candidate_list = cond2(candidate_list)
    r, c = cond3(candidate_list)
    board[r][c] = students[0]

print(level_of_satisfaction(board))
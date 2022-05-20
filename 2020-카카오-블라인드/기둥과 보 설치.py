class Frame():
    def __init__(self, start_of_p=False, start_of_b=False, end_of_p=False, end_of_b=False) -> None:
        self.start_of_pillar: bool = start_of_p
        self.start_of_beam: bool = start_of_b
        self.end_of_pillar: bool = end_of_p
        self.end_of_beam: bool = end_of_b

    def possible(self):
        # 기둥
        return self.end_of_pillar or self.end_of_beam or self.start_of_beam

    def pillar_sanity(self):
        return self.start_of_pillar == None or self.start_of_beam or self.end_of_beam or self.end_of_pillar

    def beam_sanity(self):
        return self.start_of_beam == None or (self.start_of_beam and self.end_of_beam) or self.end_of_pillar


def solution(n, build_frame):

    # 0. n+1 by n+1 짜리 board 생성
    board = [[Frame() for _ in range(n+1)] for __ in range(n+1)]
    for y in range(1):
        for x in range(n+1):
            board[y][x].end_of_pillar = True
    # 1. [x, y, a, b] 형식의 여러 입력 받기
    for op in build_frame:
        # 2. x, y(board[y][x]) 위치에 a 구조물 1: 설치하거나 0: 삭제
        x, y, a, b = op
        if a == 0:
            #   2-1. 기둥 설치:
            #       2-1-1. board[y][x]가 바닥이거나, 다른 기둥의 끝자락이거나, 보의 한쪽 끝이라면,
            #       2-1-2. board[y][x]에 기둥 표시, board[y-1][x]에 기둥 끝자락 표시
            #       기둥: 밑면이 바닥? 보의 한쪽 끝? 다른 기둥 위?
            if b == 1:
                if y == 0 or board[y][x].possible():
                    board[y][x].start_of_pillar = True
                    board[y+1][x].end_of_pillar = True
    #   2-2. 기둥 삭제:
    #       2-2-1. board[y-1][x]에 기둥
    #       2-2-2. board[y][x]에 기둥 삭제, board[y-1][x]에 기둥 끝자락 삭제
            else:
                board[y][x].start_of_pillar = False
                board[y+1][x].end_of_pillar = False
                if board[y+1][x].pillar_sanity() == False \
                        or board[y+1][x].beam_sanity() == False \
                        or board[y+1][x-1].beam_sanity() == False:
                    board[y][x].start_of_pillar = True
                    board[y+1][x].end_of_pillar = True
        elif a == 1:
            #   2-3. 보 설치: board[y][x]에 보 표시, board[y][x+1]에 보 끝자락 표시
            #       보: 한쪽 끝이 기둥 위? 양쪽 끝이 모두 보?
            if b == 1:
                if board[y][x].end_of_pillar or board[y][x+1].end_of_pillar or (board[y][x].end_of_beam and board[y][x+1].start_of_beam):
                    board[y][x].start_of_beam = True
                    board[y][x+1].end_of_beam = True
    #   2-4. 보 삭제: board[y][x]에 보 삭제, board[y][x+1]에 보 끝자락 삭제
            else:
                board[y][x].start_of_beam = False
                board[y][x+1].end_of_beam = False
                if board[y][x-1].beam_sanity() == False \
                        or board[y][x+1].beam_sanity() == False \
                        or board[y+1][x].pillar_sanity() == False:
                    board[y][x].start_of_beam = True
                    board[y][x+1].end_of_beam = True

    answer = []
    for y in range(n+1):
        for x in range(n+1):
            if board[y][x].start_of_pillar:
                answer.append([x, y, 0])
            if board[y][x].start_of_beam:
                answer.append([x, y, 1])
    # 오름차순 x좌표 정렬, y좌표 정렬, 기둥이 보보다 앞에
    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer


# n = 5
# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    # 2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1],
               [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1],
               [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0],
               [2, 2, 0, 1]]

res = solution(n, build_frame)
print(res == [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1],
      [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]], "✅")
print(res == [[0, 0, 0], [0, 1, 1], [1, 1, 1],
      [2, 1, 1], [3, 1, 1], [4, 0, 0]], "✅")


def check(board):
    board: list[list[Frame]] = []
    for y in range(n+1):
        for x in range(n+1):
            # 기둥
            if not(y == 0 or board[y][x-1].end_of_beam or board[y][x-1].start_of_beam or board[y][x].end_of_pillar):
                return False
            # 보
            # if not(board[y][x].end_of_beam and board[y][x+1].start_of_beam or board[y][x].end_of_pillar):
            if not (board[y][x].end_of_pillar or (board[y][x-1].start_of_beam and board[y][x+1].start_of_beam)):
                return False
    return True

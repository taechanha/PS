from itertools import combinations as C
from tabnanny import check


def marshal(keys): #아 생각해보니까 똑같이 동작하네;;;
    # [(0,), (1,), (2,), (3,)] -> [0, 1, 2, 3]
    # [(1, 2), (1, 3), (2, 3)] -> [[1, 2], [1,3], [2, 3]]
    marshalized = []
    for key in keys:
        temp = []
        for each in key:
            temp.append(each)
        marshalized.append(temp)
    return marshalized

def listize(keys):
    # [(0,), (1,), (2,), (3,)] -> [0, 1, 2, 3]    
    # [(1, 2), (1, 3), (2, 3)] -> [1, 2, 3]
    temp = set()
    for key in keys:
        for each in key:
            temp.add(each)
    return list(temp)

def is_uniq(keys, relation):
    """ 
    keys: [(0,), (1,), (2,), (3,)] 
          [(1, 2), (1, 3), (2, 3)]
    relation: 
        [["100", "ryan", "music", "2"], 
        ["200", "apeach", "math", "2"], 
        ["300", "tube", "computer", "3"], 
        ["400", "con", "computer", "4"], 
        ["500", "muzi", "music", "3"], 
        ["600", "apeach", "music", "2"]]
    """
    
    n = len(relation)
    m = len(relation[0])
    for key_col in keys:
        temp = set()
        for i in range(n):
            temp.add(relation[i][key_col])
        
        if len(temp) == n:
            keys.pop(key_col)
    
    return listize(keys)

# answer: 조건을 만족하는 속성의 개수
# 1. uniqueness: is_uniq()
#    - 각 열의 모든 행이 중복없는 요소로 이루어져 있는지?
# 2. minimality: is_mini()
#    - 더 적은 속성으로는 식별할 수 없는지?

# 앞에서부터 차례대로 진행하면 minimality 자연스럽게 적용됨.
def solution(relation):
    keys = range(0, len(relation))

    step = 1
    while step <= len(keys):

        # 1. 0, 1, 2, 3 열에 대해, 중복 행 포함 여부 확인
        # 2. 포함하고 있다면, 해당 열 제외
        
        # step 1에서 0이 제거되었다면 다음 step에서는 [1,2,3] 셋으로 진행.
        # 반복

        # 어떤 하나의 열에 대해 중복 행 포함 여부 확인 코드
        def is_repet(relation, c):
            n = len(relation)
            temp = set()
            for r in range(n):
                temp.add(relation[r][c])

            return len(temp) != n
        # 처음에는 하나씩
        temp_del_keys = []
        for i, key in enumerate(keys):
            if is_repet(relation, key):
                temp_del_keys.append(i)
        # key 삭제
        
        # 1st step #
        # [0, 1, 2, 3]
        keys = C(keys, step)
        # [(0,), (1,), (2,), (3,)]
        keys = is_uniq(keys)
        # [1, 2, 3]

        # 2nd step #
        # [1, 2, 3]
        keys = C(keys, step)
        # [(1, 2), (1, 3), (2, 3)]
        keys = is_uniq(keys)
        # [1]

        # terminated.

    # 1. 1개 짜리 키 하나에 대해서 uniq 확인하고, 참이면 keys에서 제외하고 cnt + 1
    # 2. 나머지 키들은 앞에서부터 2개씩 Ex. (2 3), (2, 4)씩 uniq 확인하고 참이면 둘 다 keys에서 제외
    # 3. 남아있는 keys의 개수가 현재 combination하는 step보다 작다면 종료
    #   : 제대로 종료되나?
    #       -> 다 깔끔하게 제거되서 keys가 비어있으면 step보다 당연히 작을테니 종료, 1 이상은 자명하게 종료.

    # 1 2 3 4
    # -> 1 2 | 1 3 | 14
    #    2 3 | 2 4
    #    3 4

    # -> 2 3 4

    answer = 0
    return answer


relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]
res = solution(relation)
print(res)

from itertools import combinations as C

def already_polled(columns, prev_polled):
    flag = False
    for each in prev_polled:
        if set(each).issubset(set(columns)):
            return True
    return flag

def is_valid(columns):
    uniques = set()
    temp = []
    identifiable = True
    for column in columns: # (0,) or (1, 3) etc.
        # check if this column i can be polled
        for r in range(rows):
            temp.append(relation[r][column])
    
    n = len(columns)
    for row in range(rows):
        new = []
        for i in range(n):
            new.append(temp[row + i*rows])
        uniques.add(str(new))

    if len(uniques) != rows:
        identifiable = False
    return identifiable

def solution(relation):
    global rows, polled
    res = 0

    # for all combs (nC1, nC2, nC3, nC4, ... nCn)
    n = len(relation[0])
    candidates = range(n)
    polled = []
    rows = len(relation)
    for r in range(1, n+1): # max: 8
        prev_polled = polled[:]
        for comb_case in C(candidates, r): # max: 40,000
            if already_polled(comb_case, prev_polled):
                continue
            if is_valid(comb_case):
                polled.append(comb_case)
                res += 1
    return res


relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

relation = [["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"]]

res = solution(relation)
print(res)


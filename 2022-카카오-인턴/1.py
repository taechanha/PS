
def solution(survey, choices):
    answer = None
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    d = {'AN': [0, 0], 'CF': [0, 0], 'JM': [0, 0], 'RT': [0, 0]}

    for poll, choice in zip(survey, choices):
        # AN, 5 -> N += 1
        # AN, 1 -> A += 3

        # NA, 5 -> A += 1
        # NA, 1 -> N += 3
        target = ''.join(sorted(poll))
        if choice < 5:
            if target == poll:
                d[target][0] += score[choice]
            else:
                d[target][1] += score[choice]
        else:
            if target == poll:
                d[target][1] += score[choice]
            else:
                d[target][0] += score[choice]
    
    answer = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N':0 } # RT CF JM AN
    for mbti, grades in d.items():
        if grades[0] == grades[1]:
            answer[mbti[0]] = 1
        else:
            if grades[0] > grades[1]:
                answer[mbti[0]] = 1
            else:
                answer[mbti[1]] = 1
    
    res = ''
    for k, v in answer.items():
        if v == 1:
            res += k
    return res

# 'TCMA'
# survey = ["AN", "CF", "MJ", "RT", "NA"]	
# choices = [5,3,2,7,5]
survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
res = solution(survey, choices)

print("answer: ", res)
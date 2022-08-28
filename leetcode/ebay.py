def solution(stones, k):
    answer = ''
    for i in range(len(stones)):
        if stones[i] == k:
            answer += str(i)
            break
        elif stones[i] > k:
            answer += str(i)
            break
        else:
            answer += str(i)
            stones[i] += 1
            for j in range(i+1, len(stones)):
                stones[j] -= 1
    if answer == '':
        return '-1'
    else:
        return answer


print(solution([4, 2, 2, 1, 4], 1))

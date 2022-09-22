from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)

    cnt = 0
    while s1 != s2:
        if s1 > s2:
            elem = q1.popleft()
            q2.append(elem)
            s1 -= elem
            s2 += elem
        else:
            elem = q2.popleft()
            q1.append(elem)
            s1 += elem
            s2 -= elem
        
        if cnt > len(q1) + len(q2):
            return -1
        cnt += 1

    return cnt

# test cases
for q1, q2, result in [[[3, 2, 7, 2], [4, 6, 5, 1], 2], \
                      [[1, 2, 1, 2], [1, 10, 1, 2], 7], \
                      [[1, 1], [1, 5], -1]]:
    
    my_result = solution(q1, q2)
    print("answer: ", my_result)
    assert my_result == result
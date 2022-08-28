# people	           limit	return
# [70, 50, 80, 50]	100	      3
# [70, 80, 50]	    100	      3

def solution(people, limit):
    people.sort()
    cnt = 0
    start = 0
    end = len(people) - 1
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        cnt += 1

    if start == end:
        cnt += 1
    return cnt


people = [50, 70, 80]
limit = 100
print(solution(people, limit))

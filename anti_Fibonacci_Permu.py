from itertools import permutations

def is_anti_fibonacci(each):
    if len(each) < 3:
        return True

    for i in range(len(each) - 2):
        if each[i + 2] == each[i] + each[i + 1]:
            return False

    return True


t = int(input())

while t:
    t -= 1

    n = int(input())
    cnt = 0
    
    arr = list(range(1, n + 1))
    arr = list(permutations(arr))
    
    for each in arr:
        if is_anti_fibonacci(each):
            if cnt == n:
                break
            print(*each)
            cnt += 1



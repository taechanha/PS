# 7:16 ~

# 5 1
# 5,6,3,9,-1

def calculate(k, arr):
    for _ in range(k):
        new_arr = []
        for i in range(len(arr)-1):
            new_arr.append(arr[i+1] - arr[i])
        arr = new_arr[:]
    return arr


def get_answer(arr):
    return ','.join(map(str, arr))


_, k = map(int, input().split())
arr = list(map(int, input().split(',')))
arr = calculate(k, arr)

# answer
answer = get_answer(arr)
print(answer)

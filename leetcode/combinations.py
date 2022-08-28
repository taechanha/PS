n, k = map(int, input().split())
array = list(range(1, n + 1))
array_of_set = []
chosen = []


def dfs(chosen, start, k):
    if k == 0:
        # if chosen not in array_of_set:
        array_of_set.append(chosen.copy())
    else:
        for i in range(start, n):
            chosen.append(array[i])
            dfs(chosen, i + 1, k - 1)
            chosen.remove(array[i])


dfs(chosen, 0, k)
print(array_of_set)

#     1 2 3 4

#     1            2       3
#  2  3  4      3    4   4

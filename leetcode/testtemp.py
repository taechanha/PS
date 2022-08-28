def LSB(i):
    return i & -i


def prefixSum(tree, i):
    sum = 0
    while i > 0:
        sum += tree[i]
        i -= LSB(i)
    return sum


def rangeSum(tree, i, j):
    if j < i:
        return None
    return prefixSum(tree, j) - prefixSum(tree, i - 1)


def update(tree, i, x):
    while i < n + 1:
        tree[i] += x
        i += LSB(i)


def construct_tree(arr):
    N = len(arr) + 1
    tree = [0] + arr.copy()

    for i in range(1, N):
        j = i + LSB(i)
        if j < N:
            tree[j] += tree[i]
    return tree


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = construct_tree(arr)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(tree, b, c - arr[b - 1])
        arr[b - 1] = c  # ㅋㅋㅋㅋㅋㅋ
    else:
        print(rangeSum(tree, b, c))

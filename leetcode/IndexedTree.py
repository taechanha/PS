def assertion(true, to_be_true):
    return true == to_be_true


def LSB(i):
    # 1.naive approach
    # return pow(2, bin(i)[2:][::-1].index('1'))
    # 2. better approach
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
    while i < len(tree):  # len(tree) or len(arr)
        tree[i] += x
        i += LSB(i)
    return tree
# 1. naive approach: O(nlogn)


def construct_tree(arr):
    tree = [0] * len(arr)
    for i in range(1, len(tree)):
        update(tree, i, arr[i])
    return tree

# 2. better approach O(n)


# def construct_tree(arr):
#     N = len(arr)
#     tree = arr.copy()

#     for i in range(N):
#         j = i + LSB(i)
#         if j < N:
#             tree[j] += tree[i]
#     return tree


#
# for i in range(1, 10):
    # print(assertion(i & -i, LSB(i)))

# ----------------------test--------------------------------

# init array
N = int(input())
arr = [0] + list(map(int, input().split()))

tree = construct_tree(arr)
print(tree)
tree = update(tree, 1, 3)
print(rangeSum(tree, 1, 3))

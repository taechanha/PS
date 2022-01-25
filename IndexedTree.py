def LSB(i):
    return pow(2, bin(i)[2:][::-1].index('1'))


def assertion(true, to_be_true):
    return true == to_be_true


def getSum(i):
    sum = 0
    while i > 0:
        sum += tree[i]
        i -= LSB(i)
    return sum


def rangeSum(i, j):
    return getSum(i) - getSum(j - 1)


#
for i in range(1, 10):
    print(assertion(i >> i & 1, LSB(i)))

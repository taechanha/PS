def solution(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return lcm(arr[0], arr[1])
    else:
        return lcm(arr[0], solution(arr[1:]))


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

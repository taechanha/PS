si = input
N, W = map(int, si().split())
apples = list(map(int, si().split()))

def numBoxes(i, weightLeft, boxes) -> int: # the number of boxes needed to put all apples in
    """ 
    i: int, index
    weightLeft: int
    boxes: int, used boxes
    """
    if weightLeft < 0:
        return float('inf')
    if i == N:
        return boxes
    
    # put an apple in
    case1 = numBoxes(i+1, weightLeft-apples[i], boxes)
    # make new box & put an apple in
    case2 = numBoxes(i+1, W-apples[i], boxes+1)
    return min(case1, case2)
    
ans = numBoxes(0, W, 0)
print(ans)
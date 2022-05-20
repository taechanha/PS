from typing import *


def permute(nums: List[int]) -> List[List[int]]:

    def dfs(elems):
        if len(elems) == 0:
            result.append(prev_elems[:])
        else:
            for e in elems:
                next_elems = elems[:]
                next_elems.remove(e)

                prev_elems.append(e)
                dfs(next_elems)
                prev_elems.pop()

    result = []
    prev_elems = []
    dfs(nums)

    return result


print(permute([1, 2, 3]))




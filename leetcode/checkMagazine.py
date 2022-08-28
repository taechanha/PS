#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

# case sensitive
# only whole words avail in magazine; no substring, concat
# return - Yes if else no
import collections


def checkMagazine(magazine, note):
    magazine_dict = collections.defaultdict(int)
    note_dict = collections.defaultdict(int)

    for word in magazine:
        magazine_dict[word] += 1
    for word in note:
        magazine_dict[word] -= 1

    for k, v in magazine_dict.items():
        if v < 0:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

#!/bin/python3

import math
import os
import random
import re
import sys


def stringAnagram(dictionary, query):
    answer = []
    hash_map = dict()

    for word in query:
        sorted_word = "".join(sorted(word))
        hash_map[sorted_word] = 0

    for word in dictionary:
        sorted_word = "".join(sorted(word))
        if sorted_word in hash_map:
            hash_map[sorted_word] += 1

    for k, v in hash_map.items():
        answer.append(v)

    return answer


if __name__ == '__main__':
    fptr = open('input003.txt', 'r')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

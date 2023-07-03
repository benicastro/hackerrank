# Lonely Integer #####################################################################################################################################################

# Given an array of integers, where all elements but one occur twice, find the unique element.

# Function Description ###

# Complete the lonelyinteger function in the editor below.
# lonelyinteger has the following parameter(s):
#   - int a[n]: an array of integers
# Returns
#   - int: the element that occurs only once

# Input Format ###
# The first line contains a single integer, n, the number of integers in the array.
# The second line contains n space-separated integers that describe the values in a.

# CODE ###############################################################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    a_len = len(a)
    hash_table = dict()
    for i in range(a_len):
        if a[i] in hash_table.keys():
            hash_table[a[i]] += 1
        else:
            hash_table[a[i]] = 1

    min_count = a_len + 1
    lowest_count = -1

    for j in hash_table:
        if min_count >= hash_table[j]:
            lowest_count = j
            min_count = hash_table[j]

    return lowest_count


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)

    # fptr.write(str(result) + "\n")

    # fptr.close()

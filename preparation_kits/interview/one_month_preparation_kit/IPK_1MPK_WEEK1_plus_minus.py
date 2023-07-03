# Plus Minus #####################################################################################################################

# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal
# value of each fraction on a new line with 6 places after the decimal.

# Function Description ###
# Complete the plusMinus function in the editor below.
# plusMinus has the following parameter(s):
#   - print arr[n]: an array of integers

# Input Format ###
# The first line contains an integer, n, the size of the array.
# The second line contains n space-separated integers that describe arr[n].

# Output Format ###
# Print the following  lines, each to  decimals:
# 1. proportion of positive values
# 2. proportion of negative values
# 3. proportion of zeros


# CODE #############################################################################################################################

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    sum_pos = 0
    sum_neg = 0
    sum_zero = 0
    for i in range(len_arr):
        if arr[i] > 0:
            sum_pos += 1
        elif arr[i] < 0:
            sum_neg += 1
        else:
            sum_zero += 1

    pos_prop = f"{(sum_pos / len_arr):.6f}"
    neg_prop = f"{(sum_neg / len_arr):.6f}"
    zero_prop = f"{(sum_zero / len_arr):.6f}"

    print(f"{pos_prop}\n{neg_prop}\n{zero_prop}")


# def plusMinus(arr):
#     # Write your code here
#     print("%.6f" % (len(list(filter(lambda x: (x > 0), arr)))/len(arr)))
#     print("%.6f" % (len(list(filter(lambda x: (x < 0), arr)))/len(arr)))
#     print("%.6f" % (len(list(filter(lambda x: (x ==0), arr)))/len(arr)))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
